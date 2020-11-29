import speech_recognition as sr
from gpiozero import RGBLED, Button
from time import sleep
r = sr.Recognizer()

led = RGBLED(red=4, green=2,blue=1)

while True:
    try:
        with sr.Microphone() as source:    
            # r.adjust_for_ambient_noise(source)
            r.energy_threshold(20)
            data = r.record(source, duration=3)
            text = r.recognize_google(data,language='en')
            test = {"help", "swag","penis"}
            if any(word in text for word in test):
                print("YOU SAID KEYWORD LETS GOOOOOOOOOOO")
                print("LED should now be red")
                led.color = (1,0,0)
                sleep(1)

            print(text)
    
    except Exception as e:
        print("FAIL/NOTHING IS DETECTED")
        led.color = (0,0,1)
        sleep(1)
        pass