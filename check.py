import speech_recognition as sr
r = sr.Recognizer()
while(True):
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source,duration = 5)
        print("Processing.....")
    try:
        print("I think you said:\n" + r.recognize_google(audio))
    except:
        pass
