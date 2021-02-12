#!/usr/bin/python3

from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from signal import pause
import blinkt

factory = PiGPIOFactory(host='10.10.1.8')

def red():
        global r
        global g
        global a
        if r != 1:
                r = 1
                g = 0
                a = 0
                blinkt.set_all(125,0,0)
                blinkt.show()
                blinkt.clear()
def green():
        global r
        global g
        global a
        if g != 1:
                g = 1
                r = 0
                a = 0
                blinkt.set_all(0,125,0)
                blinkt.show()
        blinkt.clear()

def amber():
        global r
        global g
        global a
        if a != 1:
                a = 1
                r = 0
                g = 0
                blinkt.set_all(255,191,0)
                blinkt.show()
        blinkt.clear()

b1 = Button(2, pin_factory=factory)
b2 = Button(3, pin_factory=factory)
b3 = Button(4, pin_factory=factory)
r = 0
g = 0
a = 0
try:
        b1.when_pressed = red
        b2.when_pressed = green
        b3.when_pressed = amber
        pause()
finally:
        r = 0
        g = 0
        pass

