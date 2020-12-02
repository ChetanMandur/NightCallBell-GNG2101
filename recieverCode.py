from bluedot.btcomm import BluetoothServer
from signal import pause
from gpiozero import RGBLED, Button, LED
from time import sleep



led = LED(2)  #Pin layout for the LED
button = Button(4) #Pin layout for button
waiting = False #Checks if the receiver got sent a signal

##Start animation
for i in range(2):
    led.on()
    sleep(1)
    led.off()
    sleep(1)


##This function will run each time the button is pressed
def button_pressed(): 
    global waiting
    if (waiting):
        print("accepting keyword")
        led.off()
        s.send("keyword receieved")
        waiting = False
    else:
        print("bell did not send an active signal")
    

        
##This function will run each time data is received from the server
def data_received(data):
    global waiting
    if (data == "stop detected"):
        print("stop detected")
        waiting = False
        led.off()

    elif (data == "keyword detected"):
        print(data)
        waiting = True
        led.on()
        

button.when_pressed = button_pressed #Tells the button what function to run when pressed
s = BluetoothServer(data_received) #Initiate the receiver

##Main look that runs forever (or until keyboard interuption)
while True:
    pause()