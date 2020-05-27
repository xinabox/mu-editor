# Imports
from machine import Pin, I2C, Timer
import network
import time
import esp32
import micropython
import sys

# Special for CW02
sdaPin = const(21)
sclPin = const(22)
redPin = const(25)
grnPin = const(26)
bluPin = const(27)

# Generic ESP32
micropython.alloc_emergency_exception_buf(100)


class myI2C:
    def __init__(self):
        self.i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin))

    def scan(self):
        print("Scanning xBus...", end="")
        devices = self.i2c.scan()
        if len(devices) > 0:
            print("found:", len(devices), "xChip(s)", end="")
            for device in devices:
                print(",", hex(device), end="")
        else:
            print("no xChips found!", end="")
        print()


class myNetwork:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def scan(self):
        print("Scanning networks...", end="")
        SSIDs = self.wlan.scan()
        if len(SSIDs) > 0:
            print("found:", len(SSIDs), "networks", end="")
            for SSID in SSIDs:
                print(", {}({})".format(SSID[0].decode(), SSID[3]), end="")
        else:
            print("no network found!", end="")
        print()


class myLEDs:
    rgb = 0

    def __init__(self):
        self.leds = [Pin(redPin, Pin.OUT), 
                     Pin(grnPin, Pin.OUT), 
                     Pin(bluPin, Pin.OUT)]
        self.pattern = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def toggle(self):
        self.rgb += 1
        for led, val in zip(self.leds, self.pattern[self.rgb % 3]):
            led.value(val)

    def allOff(self):
        for led in self.leds:
            led.value(0)


xChip = myI2C()
xinabox = myNetwork()
LED = myLEDs()

tim = Timer(-1)
tim.init(period=100, callback=lambda t: LED.toggle())
for _ in range(10):
    xChip.scan()
    time.sleep(0.1)
xinabox.scan()
print(
    "Temperature: {:.2f} C".format((esp32.raw_temperature() - 32) * 5 / 9)
)
_, mpv, mpy = sys.implementation
mpv = '.'.join(map(str,mpv))
print("This ran on Python v.{}, uPython v.{}, mpy v.{}".format(sys.version,mpv,mpy))
tim.deinit()
tim.init(period=50, mode=Timer.ONE_SHOT, callback=lambda t: LED.allOff())


