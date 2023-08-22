import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init('sapi5')  # Use the 'sapi5' engine

def talk(text):
    machine.say(text)
    machine.runAndWait()

def get_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            instruction = listener.recognize_google(audio).lower()
            print("You said:", instruction)
            return instruction
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("There was an error connecting to Google's servers.")
        return None

def play_jarvis():
    instruction = get_instruction()

    if instruction:
        print(instruction)
        if "play" in instruction:
            song = instruction.replace("play", "").strip()
            talk("Playing " + song)
            pywhatkit.playonyt(song)
        elif "time" in instruction:
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk("Current time " + time)
        elif "date" in instruction:
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            talk("Today's date " + date)
        elif "how are you" in instruction:
            talk("I am fine, how about you?")
        elif "what's your name" in instruction:
            talk("I am Jarvis, what can I do for you?")
        elif "who is" in instruction:
            human = instruction.replace("who is", "")
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
        else:
            talk("Please repeat")
    else:
        talk("I'm sorry, I didn't catch that.")

if __name__ == "__main__":
    play_jarvis()
