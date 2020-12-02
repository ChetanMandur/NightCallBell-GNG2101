from gpiozero import RGBLED, Button
from colorzero import Color
from time import sleep

led = RGBLED(red=9, green=10,blue=11) ##Grabs the pins for the RGB led


while True:
    led.color = Color('red')
    sleep(1)
    led.color = Color('green')
    sleep(1)
    led.color = Color('blue')
    sleep(1)


