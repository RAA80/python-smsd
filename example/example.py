#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from time import sleep
from serial import Serial

from smsd.client import Client
from smsd.device import SMSD42

logging.basicConfig(level=logging.INFO)


transport = Serial(port="COM5", parity='E', timeout=0.1)
id_smsd = Client(transport=transport, device=SMSD42, unit=1)
print (id_smsd)

print ("ST: {}".format(id_smsd.setParam("ST")))
print ("EN: {}".format(id_smsd.setParam("EN")))
print ("Move: {}".format(id_smsd.move(speed=100, steps=1000, edge=None)))

sleep(15)

print ("DS: {}".format(id_smsd.setParam("DS")))
