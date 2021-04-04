import os
import requests
from time import sleep
import pyttsx3

def speek(message):
        eng = pyttsx3.init()
        eng.setProperty('rate',140)
        voices=eng.getProperty('voices')
        eng.say('{}'.format(message))
        eng.runAndWait()

url = 'https://www.google.com/'
while True:
    try:
        res = requests.get(url)
        if res.status_code == 200 :
            speek('congratulation you are connected to the internet')
            break
    except Exception :
        sleep(2)
        print('Not connected')
