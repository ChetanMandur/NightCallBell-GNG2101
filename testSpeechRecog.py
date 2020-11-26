import speech_recognition as sr
r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:    
            r.adjust_for_ambient_noise(source)
            data = r.record(source, duration=5)
            text = r.recognize_google(data,language='en')
            print(text)
    
    except Exception as e:
        print("FAIL/NOTHING IS DETECTED")
        pass
        