from bluedot import BlueDot #pip install bluedot
from bluedot.btcomm import BluetoothClient # https://bluedot.readthedocs.io/en/latest/btcommapi.html
from signal import pause
from gpiozero import RGBLED, Button
from time import sleep
import speech_recognition as sr

r = sr.Recognizer()

led = RGBLED(red=9, green=10,blue=11)

def data_recieved(data):
    print(data)
    led.color = (0,0,0)
    print("receiver pressed the button")


c = BluetoothClient("raspberrypi", data_recieved)

while True:
    try:
        with sr.Microphone() as source:    
            # r.adjust_for_ambient_noise(source)
            r.energy_threshold(50)
            data = r.record(source, duration=3)
            text = r.recognize_google(data,language='en')
            test = {"help", "swag"}
            if any(word in text for word in test):
                print("keyword detected")
                c.send("keyword detected")
                led.color = (1,0,0)
                # pause()
                

            print(text)
    
    except Exception as e:
        print("FAIL/NOTHING IS DETECTED")
        pass
        