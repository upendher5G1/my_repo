import pyttsx3 as p3
import datetime
import webbrowser
import pyjokes
engine=p3.init()
engine.setProperty('rate',120)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wish_me():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12 :
        print("Good Morning sir")
        speak("Good Morning sir i am jarvis how can i help you")
    elif hour>=12 and hour<18:
        print("Good Afternoon sir")
        speak("Good Afternoon sir i am jarvis how can i help you")
    else:
        print("Good Evening sir")
        speak("Good Evening sir i am jarvis how can i help you")
def tell_time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    print("the time is:",time)
    speak(time)
def open_google():
    print("opening google")
    speak("Opening Google")
    webbrowser.open("https://google.com")
def open_youtube():
    print("opening youtube")
    speak("Opening YouTube")
    webbrowser.open("https://youtube.com")
def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)
wish_me()
while True:
    command = input("Enter command: ").lower()
    if command=="time":
        tell_time()
    elif command=="google":
        open_google()
    elif command=="youtube":
        open_youtube()
    elif command=="joke":
        tell_joke()
    elif command =="exit":
        print("Goodboy Sir")
        speak("Goodbye Sir")
        break
    else:
        print("Sorry, I did not understand")
        speak("Sorry, I did not understand")