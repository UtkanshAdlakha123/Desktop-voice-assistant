import pyttsx3 # it helps o convert text to speech
import datetime # this will tell us about the date  & time
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import pyjokes
import subprocess
import ctypes
import winshell
import requests
from datetime import date

#now we'll create our engine
engine=pyttsx3.init('sapi5') # we use this to take the inbuilt voices of our machine & sapi5 here is an API
voices=engine.getProperty('voices') # so here we get 2 voices one is of male & one is of female
# print(voices)
# now we se the voice of our machine is of male
engine.setProperty('voice',voices[0].id) # so here we take the male voice id

def speak(audio): # first func. we create is our speak func. with help of it our machine can speak
    engine.say(audio)
    engine.runAndWait() # with help of this func. our machine can speak

def wishme(): # this function whishes me 
    hour=int(datetime.datetime.now().hour) # with help of this func. we get the current time

    if hour>=0 and hour<12:
        speak("Good morning")
    
    elif hour>=12 and hour<16:
        speak("Good afternoon")

    elif hour>16 and hour<20:
        speak("Good evening")
    
    else:
        speak("Good night")
    
    speak("Hello this is Jack")

def takeCommand(): # it takes audio input from microphone & returns the string output   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold=500
        audio=r.listen(source)

    try:
        print("Recognizing.............")
        query=r.recognize_google(audio,language='en-in') # Using google for voice recognition
        print(f"User said:{query}\n") # User query will be printed

    except Exception as e:
        print("Say that again please")
        return "None"

    return query

if __name__=='__main__':
    wishme()
    
    command=takeCommand().lower()

    # Now lets write the logics for actions
    #Skill-1 is to extract something from wikipedia, first import the wikipedia module

    while True:
        
        #So here if we want to search something on wikipedia so we can from here
        if 'wikipedia' in command:
            speak("Searching the wikipedia")
            command=command.replace("wikipedia","")
            results=wikipedia.summary(command,sentences=3) # ye basically ek string de denge 3 lines ki wikipedia se uthake
            speak("According to Wikipedia")
            speak(results)

        # Now for opening the youtube we use web browser module, which will open the youtube.com for us
        elif 'open youtube' in command:
            speak("Opening Youtube")
            webbrowser.open("Youtube") # here we uses the webbrowser module to open youtube

        # it will lock the window, here we lock it with help of ctype module
        elif 'lock window' in command:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        # here we can shutdown the PC with the help of subprocess module
        elif 'shutdown system' in command:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
        
        #here we can clear the recycle bin using winshell module
        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        # here we can see the match using webbrowser
        elif 'match score' in command:
            speak("These matches are going live")
            webbrowser.open("espncricinfo.com") # here we uses the webbrowser module to open the matchscore

        # with help of webbrowser we can open google
        elif 'open google' in command:
            speak("Open Google")
            webbrowser.open("google.com") # here we uses it for opening google
        
        # Now we can play the music which is present in the pc using os directory
        elif 'play music' in command: 
            speak("Here you go with music")
            music_dir="D:\\fav-songs" # so here we first go to this directory
            songs=os.listdir(music_dir) # we store the list of songs in this variable
            
            for i in songs:
                print(i)

            son=int(input("Enter the song you want to play: "))
            print("\n")
            os.startfile(os.path.join(music_dir,songs[son])) # here we start the song with help of this func, & we join the path of that song

        # Now here we can get the current time using datetime module
        elif 'the time' in command:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") # it's the basic datetime module func.
            speak(f"Now time is:{strTime}")
        
        # Here we can get the date of current day using date module
        elif 'the date' in command:
            strDate=date.today() # we have used the date module to check the date today
            s1=strDate.strftime("%B %d,%Y")
            print(s1)
            speak(f"Today is:{s1}")
            
        # With the help of pyjokes module we can get any joke
        elif 'joke' in command:
            speak(pyjokes.get_joke()) # with help of pyjokes we get the joke
            speak("Is it a funny one!")
            strAns=takeCommand()
            
            if 'yes' in strAns:
                speak("Lmao! Ha Ha Ha")
            else:
                speak("Oh come on maan!")

        # This help me to exit from the while loop
        elif 'exit' in command:
            speak("I hope i would be helpful to you!")
            exit() # here if we want to quit 
        
        # Here we can do some chit chat
        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            str1=takeCommand()

            if 'good' in str1:
                speak("I am delighted to know that you're fine")
            
            elif 'bad' in str1:
                speak("Ohh! sorry to hear about that")

        # For news also we can open any news website
        elif 'news' in command:
            webbrowser.open("opindia.com")

        # with help of this we ca create a note & here basically we uses FILE I/O
        elif "write a note" in command:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        # we can open the file & read the note
        elif "show note" in command:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        # with the help of this we can get the weather
        elif "weather" in command:
            speak("here is the weather")
            webbrowser.open("accuweather.com")

        # here we can search anything
        elif 'search' or 'play' in command:
            command=command.replace("search","")
            command=command.replace("play","")
            webbrowser.open(command)
        