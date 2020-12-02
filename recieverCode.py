from bluedot.btcomm import BluetoothServer
from signal import pause
from gpiozero import RGBLED, Button, LED


# led = RGBLED(red=9, green=10,blue=11)
led = LED(2)
button = Button(4)
waiting = False



def button_pressed():
    print("button pressed")
    if (waiting == True):
        print("accepting keyword")
        led.off()
        s.send("keyword receieved")

def data_received(data):
    if (data == "stop detected"):
        print("stop detected")
        waiting = False
        led.off()

    elif (data == "keyword detected"):
        # print(data)
        # led.on()
        # button.wait_for_press()
        # led.off()
        # s.send("keyword recieved")
        # pause()

        print(data)
        led.on()
        waiting = True

button.when_pressed = button_pressed

s = BluetoothServer(data_received)
while True:
    pause()