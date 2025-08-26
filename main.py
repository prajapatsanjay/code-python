
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrarys  # Make sure this exists and has a 'music' dictionary

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "open spotify" in c.lower():
        webbrowser.open("https://www.spotify.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")

    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrarys.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}")
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    recognizer = sr.Recognizer()

    while True:
        # listen for the wake word "jarvis"
        # obtain audio form micrphone 
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
              print("Listening...")
              audio = r.listen(source,timeout =2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                print("yes")

                # listen for command 
                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

            speak("Sorry, I didn't catch that.")





