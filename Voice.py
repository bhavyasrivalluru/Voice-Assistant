try:
    import speech_recognition as sr
    HAS_SPEECH_RECOGNITION = True
except Exception:
    sr = None
    HAS_SPEECH_RECOGNITION = False

try:
    import pyttsx3
    HAS_PYTTSX3 = True
except Exception:
    pyttsx3 = None
    HAS_PYTTSX3 = False

import datetime
import webbrowser
import os

try:
    import wikipedia
    HAS_WIKIPEDIA = True
except Exception:
    wikipedia = None
    HAS_WIKIPEDIA = False

try:
    import pyjokes
    HAS_PYJOKES = True
except Exception:
    pyjokes = None
    HAS_PYJOKES = False
import sys
def speak(text):
    print(f"Assistant: {text}", flush=True)
    try:
        if HAS_PYTTSX3:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        else:
            # fallback: only print (already printed above)
            pass
    except:
        print("Speech output failed or not supported in this environment.", flush=True)
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening! Bhavya")
    speak("I am your voice assistant. How can I help you today?")
def take_command():
    try:
        sys.stdout.write("You (type your command): ")
        sys.stdout.flush()
        line = sys.stdin.readline()
        if not line:
            return ""
        return line.strip().lower()
    except Exception:
        return ""
def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except:
                speak("Sorry, I couldn't find anything.")

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
            speak("Sorry, I didn't understand that. Try again.")


if __name__ == "__main__":
    try:
        run_assistant()
    except KeyboardInterrupt:
        try:
            speak("Goodbye!")
        except Exception:
            print("Goodbye!", flush=True)
