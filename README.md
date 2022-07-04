
# Desktop-Voice-Assistant

I have created a Desktop voice assitant using python. It is a voice assistant is a digital assistant that uses speech recognition, speech processing algorithms, and speech synthesis to listen to specific voice commands, return relevant information, and perform specific functions at the request of the user.



## Description

As we know Python is a competent language for scriptwriters and developers. Let’s write a script for Voice Assistant using Python. The query for the assistant can be manipulated as per the user’s need. 

Speech recognition is the process of converting audio into text. This is ordinarily used in voice assistants like Alexa, Siri, etc. Python provides an API called SpeechRecognition to allow us to convert audio into text for further processing. So here we will look at converting large or long audio files into text using the SpeechRecognition API in python.

## Features

- Open & close any application of the system
- Search anything on google like news, weather, wikipedia,etc.
- Able to speak time & date
- Play or stop music in you system
- Search anythng on youtube
- Lock the window & sleep/restart/shutdown your system.
- Can write a note for you & you can see it also

and many more.


## Tech Stack

**Programming-Language:** Python 3.10


## API reference


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `sapi5` | `string` | SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications. |


## Modules needed & Libraries

|   **Module name**   |     **Description**    |    **How to install**   |
| :-------- | :------- | :------------------------- |
| **Speech Recognition:-** | One of the most important of these when creating a speech assistant application is for the assistant to recognize your voice (meaning what you want to say / hear). | `pip install speechrecognition ` |
|**Pyttsx3:-**| This module is used by programs running offline to convert text to speech| `pip install pyttsx3` |
|**Subprocess:-**| This module is used to get the details of the system subprocess  used in various commands. B. Shutdown, sleep, etc. This module is built into Python.|`pip install subprocess`|
|**Wikipedia:-**|As you know, Wikipedia is a great source of knowledge, so here we  used the Wikipedia module to get information from Wikipedia and to do a Wikipedia search.|`pip install wikipedia`|
|**Web Browser:-** |Performs a web search. This module is built into Python. |`pip install webbrowser`|
|**Date and Time:-**| The date and time are used to display the date and time. This module is built into Python. |`pip install datetime`|
   
   
**Note**:- You can remove some of the import files if you don’t want to get that feature


**Import the below libraries**

`import pyttsx3`

`import datetime `

`import speech_recognition as sr`

`import pyaudio`

`import wikipedia`

`import webbrowser`

`import os`

`import pyjokes`

`import subprocess`

`import ctypes`

`import winshell`

`import requests`

`from datetime import date`


It is easy to build a voice assistant. You can add more features as well.
