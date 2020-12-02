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
    print(type(data))
    if (data == "stop detected"):
        print("stop detected")
        led.off()

    elif (data == "keyword detected"):
        print(data)
        led.on()
        command = input("Alert recieved. Type anything to emulate a button press")
        led.off()
        s.send("keyword recieved")
        # pause()


s = BluetoothServer(data_received)
while True:
    pause()