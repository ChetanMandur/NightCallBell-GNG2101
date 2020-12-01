from bluedot.btcomm import BluetoothServer
from signal import pause
from gpiozero import RGBLED, Button, LED


# led = RGBLED(red=9, green=10,blue=11)
led = LED(2)
button = Button(3)
# button.when_pressed = button_pressed


# def button_pressed():
#     s.send("keyword receieved")

def data_received(data):
    keyWords = {"help","hey"}
    stopWords = {"stop"}

    if (data in stopWords):
        print("stop detected")
        led.color=(0,0,0)

    elif (data in keyWords):
        print(data)
        led.color=(1,0,0)
        button.wait_for_press()
        led.color=(0,0,0)
        s.send("keyword recieved")
        # pause()


s = BluetoothServer(data_received)
while True:
    pause()