from bluedot import BlueDot #pip install bluedot
from bluedot.btcomm import BluetoothClient # https://bluedot.readthedocs.io/en/latest/btcommapi.html
from signal import pause
from gpiozero import RGBLED, Button
from colorzero import Color
from time import sleep
import speech_recognition as sr

r = sr.Recognizer() #Starts the voice recognition

led = RGBLED(red=9, green=11,blue=10) ##Grabs the pins for the RGB led

def data_recieved(data):
    print(data)
    led.color = (0,0,0)
    print("receiver pressed the button")


c = BluetoothClient("raspberrypi", data_recieved)


##Start animation
led.color = (1,0,0)
sleep(1)
led.color = (0,1,0)
sleep(1)
led.color = Color('pink')
led.blink()
led.color = (0,0,0)


while True:
    try:
        with sr.Microphone() as source:    
            r.adjust_for_ambient_noise(source)
            # r.energy_threshold = 0
            data = r.record(source, duration=3)
            text = r.recognize_google(data,language='en')
            keyWords = {"help","hey"}
            stopWords = {"stop"}

            if any(word in text for word in stopWords):
                print("stop detected")
                c.send("stop detected")
                led.color = (0,0,0)

            elif any(word in text for word in keyWords):
                print("keyword detected")
                c.send("keyword detected")
                # led.color = (1,0,0)
                led.color = Color('pink')
                
                # pause()
                

            print(text)
    
    except Exception as e:
        print("Nothing has been detected...")
        pass
        