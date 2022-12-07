import board
import digitalio as dio
import time
import neopixel
import random
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A7, echo_pin=board.A4)


num_pixels = 30
np = neopixel.NeoPixel(board.A3, num_pixels, brightness=1, auto_write=False)

"""
Name: middle
Description: This function take a color and pulses it from both ends of the LED strip to the
middle and then blackens it from the same ends
Parameters: colors(tuple) - This is the RGB value that will be pulsed. stop(floating point) - this will control how fast each pulse is
Return: none
"""
def middle(colors, stop):
    color = colors
    for i in range(0, num_pixels/2, 1):
        np[i] = color[i%len(color)]
        np.show()
        time.sleep(stop)
        np[num_pixels - 1 - i] = color[i%len(color) - 1]
        np.show()
        time.sleep(stop)
    for i in range(num_pixels):
        np[i] = (0, 0, 0)
        np.show()
        time.sleep(stop)
        np[num_pixels - 1 - i] = (0, 0, 0)
        np.show()
        time.sleep(stop)
while True:
    try:
        dist = sonar.distance
        print(dist)
        if int(dist) > 32:
            for i in range(num_pixels/3):
                np[i] = (255, 0, 0)
            np.show()
        elif int(dist) <= 32 and int(dist) > 20:
            for i in range(((num_pixels/3) * 2)):
                np[i] = (255, 255, 0)
            np.show()
        elif int(dist) <= 20:
            for i in range(num_pixels):
                np[i] = (255, 0, 255)
            np.show()
        np.fill((0, 0, 0))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
