import speech_recognition as sr

from time import sleep
r = sr.Recognizer()


while True:
    try:
        with sr.Microphone() as source:    
            # r.adjust_for_ambient_noise(source)
            r.energy_threshold = 0
            data = r.record(source, duration=5)
            text = r.recognize_google(data,language='en')
            test = {"help", "swag","penis"}
            if any(word in text for word in test):
                print("YOU SAID KEYWORD LETS GOOOOOOOOOOO")


            print(text)
    
    except Exception as e:
        print("FAIL/NOTHING IS DETECTED")

        pass