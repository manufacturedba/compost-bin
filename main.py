import time
import board
import adafruit_bme680
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

i2c = board.I2C()

# Actually a BME688
bme688 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

while True:
    print("%d C" % bme688.temperature )
    print("%d ohm" % bme688.gas)
    print("%d rH %%" % bme688.relative_humidity)
    
    # Indicate life
    pixel.fill((0, 0, 255))
    time.sleep(1)
    pixel.fill((0, 0, 0))
    time.sleep(1)