import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import pywhatkit
import pyjokes
import wikipedia

listener = sr.Recognizer()

counter = 0
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):

    engine.say(text)
    while counter>3:
        break
    else:
        engine.runAndWait()

def command_center():
    try:
        speak('Hello welcome to MyAlexa')
        counter=counter+1
        with sr.Microphone() as source:
            speak('I am ready to listen')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')    
#   if not command:
#         if counter<3:
#             speak('Ask me something') 
#             run_command()
#         else:
#             speak('Thank you Please Try after sometimes')
    except:
        pass
    return command

def run_command():
    command = command_center()
    if 'how are you' in command:
        speak('I am great how you are')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        speak('current time is '+time)
    elif 'play' in command:
        song = command.replace('play','')
        speak('playing'+song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'who' or 'what' in command:
        command = command.replace('who is','')
        command = command.replace('what is','')
        speak(wikipedia.summary(command,2))
    else:
        speak('I am still learning bot, please help with any other command')

while True:
    run_command()
