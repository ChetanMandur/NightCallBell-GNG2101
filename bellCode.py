from bluedot import BlueDot #pip install bluedot
from bluedot.btcomm import BluetoothClient # https://bluedot.readthedocs.io/en/latest/btcommapi.html
from signal import pause
import gpiozero import LED
import speech_recognition as sr

r = sr.Recognizer()

led = gpiozero.LED(7)



def data_recieved(data):
    led.off()


c = BluetoothClient("raspberrypi", data_recieved)

while True:
    try:
        with sr.Microphone() as source:    
            r.adjust_for_ambient_noise(source)
            data = r.record(source, duration=3)
            text = r.recognize_google(data,language='en')
            test = {"help", "swag"}
            if any(word in text for word in test):
                print("keyword detected")
                c.send("keyword detected")
                
                

            print(text)
    
    except Exception as e:
        print("FAIL/NOTHING IS DETECTED")
        pass
        