#!/usr/bin/env python

import os
import sys

if not os.getegid() == 0:
    sys.exit('Debes ejecutar este Script como SU')

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PA20

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

try:
    print ("Pulsa CTRL+C para salir")
    while True:
        gpio.output(led, 1)
        print "led set 1 \r\n"
        sleep(2)
        gpio.output(led, 0)
        print "led set 0 \r\n"
        sleep(2)
        gpio.output(led, 1)
        sleep(0.1)
        gpio.output(led, 0)
        sleep(0.1)
        sleep(0.6)
    
except KeyboardInterrupt:
    print ("Saliendo.")
