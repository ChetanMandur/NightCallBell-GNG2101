import speech_recognition as sr
r = sr.Recognizer()

#led = gpiozero.LED(PIN LOCATION)

while True:
    try:
        with sr.Microphone() as source:    
            r.adjust_for_ambient_noise(source)
            data = r.record(source, duration=3)
            text = r.recognize_google(data,language='en')
            test = {"help", "swag","penis"}
            if any(word in text for word in test):
                print("YOU SAID KEYWORD LETS GOOOOOOOOOOO")


                ##BELOW IS PSUEDOCODE, JUST PLANNING WHERE CODE WILL GO
                # click_mouse()
                # counter = 0
                # led.on()
                # while counter <200:
                #     counter = counter +1
                # led.off()

            print(text)
    
    except Exception as e:
        print("FAIL/NOTHING IS DETECTED")
        pass