from bluedot import BlueDot #pip install bluedot
from bluedot.btcomm import BluetoothClient # https://bluedot.readthedocs.io/en/latest/btcommapi.html
from signal import pause
from gpiozero import RGBLED, Button
from colorzero import Color
from time import sleep
import speech_recognition as sr

r = sr.Recognizer() #Starts the voice recognition

led = RGBLED(red=9, green=11,blue=10) ##Grabs the pins for the RGB led

keepGoing = True #Variable that stays true as long as reciever has not been found/connected

##Function that runs when data is recieved 
def data_recieved(data):
    print(data)
    led.color = (0,0,0)
    print("receiver pressed the button")

##Start animation
for i in range(2):
    led.color = Color('pink')
    sleep(1)
    led.color = (0,0,0)
    sleep(1)


##Loops that runs until reciever has been detected and successfully connected
while keepGoing:
    try:
        c = BluetoothClient("raspberrypi", data_recieved)
        print("Receiver found!")
        keepGoing = False
    
    except:
        print("Receiver not found... keep searching")



##Main loop for the program, runs forever (or until keyboard interuption)
while True:
    try:
        with sr.Microphone() as source: #Takes the microphone as input
            r.adjust_for_ambient_noise(source) 
            # r.energy_threshold = 0
            data = r.record(source, duration=3)
            text = r.recognize_google(data,language='en')

            #list of keywords for the bell (both activation and stop keywords)
            keyWords = {"help","hey"}
            stopWords = {"stop"}

            #runs if a stop keyword is detected
            if any(word in text for word in stopWords):
                print("stop detected")
                c.send("stop detected")
                led.color = (0,0,0)

            #runs if an activation keyword is detected
            elif any(word in text for word in keyWords):
                print("keyword detected")
                c.send("keyword detected")
                led.color = Color('pink')
                

            print(text)
    
    #Runs when no voice/speech has been detected
    except Exception as e:
        print("Nothing has been detected...")
        pass
        