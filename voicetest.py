import speech_recognition as sr
import time
from gtts import gTTS
from pygame import mixer
import pygame
import sys
import tempfile

import socket
from translate import Translator

def speak(sentence, lang, loops=1):
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        # tts.save('test.mp3')
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        # mixer.music.load('test.mp3')
        mixer.music.play(loops)
   
def music(sentence, lang, loops=1):
    mixer.init()
    screen=pygame.display.set_mode([100,100])
    pygame.time.delay(1000)
    mixer.music.load("boom.mp3")
    mixer.music.play()
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()




# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    #print("Google Speech Recognition thinks you said::>>>")
    # print(r.recognize_google(audio, language="zh-TW"))
    s = r.recognize_google(audio, language="ko-KR")
    print(s)
 
 
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("No response from Google Speech Recognition service: {0}".format(e))



if s:
      #print("Text to Speech(gTTS) repeating what you just said::<<<")
      # time.sleep(3)
   
    trans=""
    translator = Translator(from_lang="korean", to_lang="chinese")
    trans = translator.translate(s)
    #s=s.lower()
    
    server_ip='192.168.31.200'
    server_port=3334
    so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    so.connect((server_ip,server_port))
    

    if s=="왼쪽": 
        s='1'
        trans="我要去房間"
    elif s=="가운데": 
        s='2'
        trans="我要去充電處"
    elif s=="오른쪽": 
        s='3'
        trans="我要去倉庫"
    
    byt=s.encode()
    so.send(byt)
    so.close()
    
    
    speak(trans,'zh-TW',1)

    time.sleep(5)
    print('Done!')