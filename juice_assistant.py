import os
import pyttsx3 as tts
import datetime
import speech_recognition as sr
import webbrowser

print("\t\t====================================================================================")
print("\t\t\t\t\t\tJuice Personal Assistant")
print("\t\t====================================================================================")
print()

def greetme():
    currenth = int(datetime.datetime.now().hour)
    if 0 <= currenth < 12:
        tts.speak('Good Morning !')

    if 12 <= currenth < 16:
        tts.speak('Good Afternoon !')

    if 16 <= currenth < 19:
        tts.speak('Good Evening !')

    if currenth >= 19 and currenth != 0:
        tts.speak('Good Night !')

greetme()

tts.speak("Welcome to your Personal Assistant Juice")
tts.speak("Hope that you're doing well. How can I help you")

def mycommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        tts.speak("Sorry sir! I didn't get that! Try typing the command!")
        query = str(input('Command: '))

    return query

while True:
    query = mycommand().lower()
    print("query is ", query)

    if ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ( ("chrome" in query) or ("browser" in query) ):
        os.system("start chrome")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("notepad" in query):
        os.system("start notepad")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("firefox" in query):
        os.system("start firefox")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("whatsapp" in query):
        os.system("C:\\Users\\mtabi\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("spotify" in query):
        os.system("start spotify")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("vlc" in query):
        os.system("start vlc")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ( ("cmd" in query) or ("terminal" in query) ):
        os.system("start cmd")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("control panel" in query):
        os.system("start control panel")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ( ("explorer" in query) or ("this pc" in query) or ("my computer") in query):
        os.system("start explorer")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("calculator" in query):
        os.system("start calc")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and (("camera" in query) or ("webcam" in query) ):
        os.system("start microsoft.windows.camera:.")
    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("google" in query):
        os.system("start chrome https://google.com")
    elif ('bye juice' in query) or ('bye' in query):
        tts.speak('Good Bye... Have a good time.')
        exit()
    else:
        tts.speak('Command not found... Try again...')

    input("Press Enter to Continue: ")

    tts.speak('Next Command! Sir!')


