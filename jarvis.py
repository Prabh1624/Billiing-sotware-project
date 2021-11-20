import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')  # sapi5 is to use window voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):  # clwill speak given arguement
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak(
        "Welcome To AP Mall!  --You are visualising the billing software. designed by two experts of their field. Master Prabh Singh. and. Abhikriti Moti")



if __name__ == "__main__":
    wishMe()
