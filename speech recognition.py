import speech_recognition as sr    
    
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Say something!")
        audio = r.listen(source)#listening to microphone
        data =r.recognize_google(audio)

while True:
    speak("what can i do for u")
    listen()
