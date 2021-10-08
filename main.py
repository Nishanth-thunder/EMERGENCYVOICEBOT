import speech_recognition as sr
import pyttsx3
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('I am Friday... Welcome to edtrek...We will make your lessons to understand better')
engine.say('If you face any issues or any emergency pls say... FRIDAY EMERGENCY')

engine.runAndWait()
wikipedia.set_lang("en")
i=0
def talk(text):
    engine.say(text)
    engine.runAndWait()
def t_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday ',' ')
                print(command)
                return command


    except:
        pass
    return command
def run_mark():
    command=t_command()
    if 'emergency' in command:
        talk('EMERGENCY! SENDING TERMINATING SIGNAL')
        exit()


    else:
        talk('i cant understand')
        exit()


while True:
    command=" "
    run_mark()
