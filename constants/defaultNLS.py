#!/usr/bin/env python3
"""
Polyglot v3 node server 7Port IR/RF
Copyright (C) 2021 Javier Refuerzo

"""





class DefaultNls() :

    nls = '''
#Controller
ND-ctl-NAME = iTach IR
ND-ctl-ICON = Output

ST-ctl-ST-NAME = NodeServer Online
ST-ctl-GV0-NAME = Module address
ST-ctl-GV1-NAME = Module Type

#irdevice
NDN-irdevice-ICON = Output
ST-irdevice-GV0-NAME = Last Error

#Shared command names

CMD-STOP-NAME = Stop IR
CMD-COMMAND-NAME = Send IR
CMDP-BUTTON-NAME = Button Name
CMDP-CODE-NAME = Alternate Codes
CMDP-CONNECTOR-NAME = Connector
CMDP-REPEAT-NAME = Repeat


ERRORS--2 = Unknown Error (see logs)
ERRORS--1 = Connection Error (see logs)
ERRORS-0 = None
ERRORS-1 = Invalid command. Command not found
ERRORS-2 = Invalid module address (does not exist).
ERRORS-3 = Invalid connector address (does not exist).
ERRORS-4 = Invalid ID value
ERRORS-5 = Invalid frequency value
ERRORS-6 = Invalid repeat value
ERRORS-7 = Invalid offset value.
ERRORS-8 = Invalid pulse count.
ERRORS-9 = Invalid pulse data.
ERRORS-10 = Uneven amount of <on|off> statements.
ERRORS-11 = No carriage return found.
ERRORS-12 = Repeat count exceeded.
ERRORS-13 = 3 IR command sent to input connector
ERRORS-14 = Blaster command sent to non-blaster connector.
ERRORS-15 = No carriage return before buffer full.
ERRORS-16 = No carriage return.
ERRORS-17 = Bad command syntax.
ERRORS-18 = Sensor command sent to non-input connector.
ERRORS-19 = Repeated IR transmission failure.
ERRORS-20 = Above designated IR <on|off> pair limit.
ERRORS-21 = Symbol odd boundary
ERRORS-22 = Undefined symbol.
ERRORS-23 = Unknown option.
ERRORS-24 = Invalid baud rate setting.
ERRORS-25 = Invalid flow control setting
ERRORS-26 = Invalid parity setting.
ERRORS-27 = Settings are locked.


CODE-1 = Button Code 1
CODE-2 = Button Code 2

CONNECTOR-1 = Output 1
CONNECTOR-2 = Output 2
CONNECTOR-3 = Output 3
CONNECTOR-4 = Output 4
CONNECTOR-5 = Output 5
CONNECTOR-6 = Output 6
CONNECTOR-7 = Output 7
CONNECTOR-8 = Output 8
CONNECTOR-9 = Output 9

MODULETYPE-0 = UNKNOWN
MODULETYPE-1 = WIFI
MODULETYPE-2 = ETHERNET
MODULETYPE-3 = 3 RELAY
MODULETYPE-4 = 3 IR
MODULETYPE-5 = 1 SERIAL

    
'''

