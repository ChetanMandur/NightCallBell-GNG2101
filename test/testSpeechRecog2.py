import speech_recognition as sr

from time import sleep
r = sr.Recognizer()

##Start animation
print("red")
sleep(1)
print("green")
sleep(1)
print("pink")
# led.blink()
#led.color = (0,0,0)
sleep(1)
print("off")


while True:
    try:
        with sr.Microphone() as source:    
            # r.adjust_for_ambient_noise(source)
            r.energy_threshold = 0
            data = r.record(source, duration=5)
            text = r.recognize_google(data,language='en')
            test = {"help", "swag","hey"}
            stopWords = {"stop"}

            if any(word in text for word in stopWords):
                print("YOU SAID STOP AHHHHHHHHHHH")

            elif any(word in text for word in test):
                print("YOU SAID KEYWORD LETS GOOOOOOOOOOO")
                


            print(text)
    
    except Exception as e:
        print("FAIL/NOTHING IS DETECTED")

        pass