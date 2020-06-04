# Imports
import time
import sys
import busio
import digitalio
from board import *


class myI2C:
    def __init__(self):
        self.i2c = busio.I2C(SCL, SDA)

    def scan(self):
        print("Scanning xBus...", end="")
        self.i2c.try_lock()
        devices = self.i2c.scan()
        self.i2c.unlock()
        if len(devices) > 0:
            print("found:", len(devices), "xChip(s)", end="")
            for device in devices:
                print(",", hex(device), end="")
        else:
            print("no xChips found!", end="")
        print()


class myLEDs:
    rgb = 0

    def __init__(self):
        r = digitalio.DigitalInOut(RED)
        r.direction = digitalio.Direction.OUTPUT
        g = digitalio.DigitalInOut(GREEN)
        g.direction = digitalio.Direction.OUTPUT
        b = digitalio.DigitalInOut(BLUE)
        b.direction = digitalio.Direction.OUTPUT

        self.leds = [r, g, b]
        self.pattern = [[True, False, False],
                        [False, True, False],
                        [False, False, True]]

    def toggle(self):
        self.rgb += 1
        for led, val in zip(self.leds, self.pattern[self.rgb % 3]):
            led.value = val

    def allOff(self):
        for led in self.leds:
            led.value = False


xChip = myI2C()
LED = myLEDs()

for _ in range(10):
    xChip.scan()
    LED.toggle()
    time.sleep(0.1)

_, mpv = sys.implementation
mpv = ".".join(map(str, mpv))
print("This ran on Python v.{}, uPython v.{},".format(sys.version, mpv))
