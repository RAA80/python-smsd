## python-smsd ##

Библиотека для работы с контроллерами шагового двигателя SMSD фирмы Электропривод

### 1. Работа с консольной версией ###

- Режим **User**

        usage: smsd-console [-h] --port [PORT] [--timeout [VALUE]] [--debug]
                            [--unit [UNIT]] [--set [KEY [VALUE ...]] | --move
                            [ARG [ARG ...]]]

        SMSD command-line option

        optional arguments:
          -h, --help                show this help message and exit
          --port [PORT]             Set used port name
          --timeout [VALUE]         Set used timeout in second
          --debug                   Print debug information

        User:
          --unit [UNIT]             Set used SMSD address
          --set [KEY [VALUE ...]]   Write config value. Possible KEY values: ['AL', 'BG',
                                    'CF', 'DL', 'DR', 'DS', 'ED', 'EM', 'EN', 'HM', 'ID',
                                    'JP', 'LB', 'LD', 'LL', 'MH', 'ML', 'MV', 'RB', 'RD',
                                    'RS', 'SB', 'SD', 'SF', 'SP', 'SS', 'ST', 'WH', 'WL']
          --move [ARG [ARG ...]]    Send move command with args: Speed, Steps, Edge

### 2. Работа с симулятором SMSD ###

	usage: smsd-simulator [-h] --port [PORT] --unit [UNIT]

	SMSD simulator command-line option

	optional arguments:
	  -h, --help     show this help message and exit
	  --port [PORT]  Set used port name
	  --unit [UNIT]  Set used SMSD address
