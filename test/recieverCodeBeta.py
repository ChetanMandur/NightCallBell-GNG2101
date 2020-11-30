from bluedot.btcomm import BluetoothServer
from signal import pause
from gpiozero import RGBLED, Button, LED


led = LED(2)
# led = RGBLED(red=9, green=10,blue=11)
# button = Button(2)
# button.when_pressed = button_pressed


# def button_pressed():
#     s.send("keyword receieved")

def data_received(data):
    print(data)
    led.on()
    # led.color=(1,0,0)
    command = input("Alert recieved. Type anything to emulate a button press")
    # led.color=(0,0,0)
    led.off()
    s.send("keyword recieved")
    # pause()


s = BluetoothServer(data_received)
while True:
    pause()