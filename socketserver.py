# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:36:10 2020

@author: kyojeong
"""
import time
import sys
import socket
from gtts import gTTS
from pygame import mixer
import pygame
import tempfile

def speak(sentence, lang, loops=1):
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        # tts.save('test.mp3')
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        # mixer.music.load('test.mp3')
        mixer.music.play(loops)

server_ip='192.168.31.102'
server_port= 9000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((server_ip,server_port))
s.listen(1)
conn,addr=s.accept()
data=conn.recv(2000)
data.decode()
print("任務結束")
speak(u"我到了請您開門",'zh-TW',1)
time.sleep(3)

server_ip='192.168.31.45'
server_port=9999
so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect((server_ip,server_port))
s="speaker"
byt=s.encode()
so.send(byt)
print("已傳送")
speak(u'請您接收','zh-TW',1)
data=so.recv(2000)
so.close()


time.sleep(5)

