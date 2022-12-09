import board
import digitalio as dio
import time
import neopixel
import random
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A7, echo_pin=board.A4)


num_pixels = 30
np = neopixel.NeoPixel(board.A3, num_pixels, brightness=1, auto_write=False)

while True:
    try:
        dist = sonar.distance
        np.fill((0, 0, 0))
        num = 30 - (dist/7)
        for i in range(int(num)):
            if dist > 0:
                np[i] = (255, 255, 255)
        np.show()

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
