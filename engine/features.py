import datetime
import os
import re
import struct
import time
import eel      # To connect Backend(Python) with Frontend(JavaScript) 
import pyaudio
import pywhatkit as kit
import sqlite3
import webbrowser
import pvporcupine

from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term
from hugchat import hugchat



con = sqlite3.connect("sabreen.db")
cursor = con.cursor()


# Playing assistant sound function
@eel.expose    # To excess it from main.js
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)



def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("please", "")
    query = query.replace("open", "")
    query.lower()    # converts all query/commands into lowerCase

    app_name = query.strip()  # to remove space

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")



def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)


def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["computer"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)   # microphone will stream continue to detect HotWord
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key windows+j
                import pyautogui as autogui
                autogui.keyDown("win")  # windows +
                autogui.press("j")   # j
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
        

# chat bot 
# def chatBot(query):
#     user_input = query.lower()
#     chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response =  chatbot.chat(user_input)
#     print(response)
#     speak(response)
#     return response


