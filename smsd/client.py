#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


class Client(object):
    ''' Класс для работы с контроллерами шагового двигателя SMSD '''

    def __init__(self, transport, device, unit):
        self._transport = transport
        self._unit = unit
        self._device = device

    def __del__(self):
        if self._transport.is_open:
            self._transport.close()

    def __repr__(self):
        return ("Client(transport={}, unit={})".format(self._transport,
                                                       self._unit))

    def _verify(self, answer):
        if answer != b"E10*":
            _logger.error("SmsdProtocolError: Write command error {}".
                          format(answer))
            return None
        return True

    def _getPingPong(self, request):
        self._transport.reset_input_buffer()
        self._transport.reset_output_buffer()

        packet = "{}{}*".format(request["command"], request["param"])

        _logger.debug("Send frame = {!r}, len={}".format(packet, len(packet)))

        for ch in packet:
            writed = self._transport.write(ch.encode("ascii"))
            answer = self._transport.read()

        answer = self._transport.read(4)

        _logger.debug("Recv frame = {!r}, len={}".format(answer, len(answer)))

        return self._verify(answer)

    def setParam(self, name, value=None):
        ''' Запись значения параметра по заданному имени '''

        _dev = self._device[name]

        if _dev != "MV" and value is not None:
            if value < _dev['min'] or value > _dev['max']:
                raise ValueError("Parameter [{}] out of range ({}, {})".
                                 format(name, _dev['min'], _dev['max']))

        request = {'command': name,
                   'param':   value if value is not None else ""}
        return self._getPingPong(request)

    def move(self, speed=None, steps=None, edge=None):
        ''' В зависимости от установленных параметров, происходит движение
            с постоянной скоростью, по шагам или до ограничителя.
            Если скорость не указана или равна 0 происходит остановка движения
        '''

        edges = ("IN1", "IN2", "HOME")
        if edge and edge not in edges:
            raise ValueError("Unknown edge. Must be 'IN1', 'IN2', 'HOME'")

        args = []
        if speed:
            args.append(("DR", None) if speed > 0 else ("DL", None))
            args.append(("SD", abs(speed)))
            args.append(("MV", steps) if steps else ("MV", None))

            if edge in edges:
                if edge == "IN1":  args.append(("ML", None))
                if edge == "IN2":  args.append(("MH", None))
                if edge == "HOME": args.append(("HM", None))
        else:
            args.append(("DS", None))

        for arg in args:
            if not self.setParam(*arg):
                return None

        return True


__all__ = [ "Client" ]
