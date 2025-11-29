import matplotlib.pyplot as plt
import pyttsx3
import pyaudio
import speech_recognition as sr
import webbrowser
import os

speaker = pyttsx3.init()
mic = sr.Recognizer()

speaker.say("Welcome TO Hemendra Radhe Radhe ")
speaker.runAndWait()
with sr.Microphone() as source:
    print("start speaking ....")
    audio = mic.listen(source)
    text = mic.recognize_google(audio)
    print(f"you said:{text}")
if "open Notepad" in text:
    print ("Opening Notepad ...")
    os.system("notepad")