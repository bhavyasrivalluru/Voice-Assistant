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
import urllib.parse

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

        elif ('date' in query) or ('today' in query and 'time' not in query):
            today = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today's date is {today}")

        elif (('order' in query) and ('food' in query or 'pizza' in query or 'delivery' in query)) or ('order food' in query):
            speak("Opening a food delivery service for you.")
            try:
                webbrowser.open("https://www.ubereats.com/")
            except Exception:
                speak("Unable to open the browser on this system.")

        elif 'play' in query and ('music' in query or 'song' in query or 'listen' in query or 'play' in query):
            # try to extract a search term; if none found, open YouTube
            search = query
            for w in ("play", "music", "song", "listen to", "listen"):
                search = search.replace(w, "")
            search = search.strip()
            if search:
                url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(search)
                speak(f"Playing {search} on YouTube.")
            else:
                url = "https://www.youtube.com/"
                speak("Opening YouTube music.")
            try:
                webbrowser.open(url)
            except Exception:
                speak("Unable to open the browser on this system.")

        elif 'joke' in query:
            if HAS_PYJOKES:
                try:
                    joke = pyjokes.get_joke()
                    speak(joke)
                except Exception:
                    speak("Sorry, I couldn't fetch a joke right now.")
            else:
                speak("Joke service is not available. Install the 'pyjokes' package to enable jokes.")

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
