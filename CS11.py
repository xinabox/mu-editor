# Imports
import time
import sys
import busio
import digitalio
from board import *
import adafruit_sdcard
import storage


class mySD:
    # Connect to the card and mount the filesystem.
    def __init__(self):
        self.spi = busio.SPI(SCK, MOSI, MISO)
        self.cs = digitalio.DigitalInOut(CS)
        self.sdcard = adafruit_sdcard.SDCard(self.spi, self.cs)
        self.vfs = storage.VfsFat(self.sdcard)
        storage.mount(self.vfs, "/sd")

    def readSD(self):
        # Use the filesystem as normal.
        with open("/sd/test.txt", "r") as f:
            for line in f:
                print(line, end="")
            print()

    def writeSD(self):
        # Use the filesystem as normal.
        with open("/sd/hello.txt", "w") as f:
            f.write("Hello world\n")


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
text = mySD()

for _ in range(10):
    xChip.scan()
    LED.toggle()
    time.sleep(0.1)

text.readSD()

_, mpv = sys.implementation
mpv = ".".join(map(str, mpv))
print("This ran on Python v.{}, uPython v.{},".format(sys.version, mpv))
