import pyttsx3 #pip install pyttsx3(text to speech)
import datetime
import speech_recognition as sr #pip install speechRecognition (input speech)
import wikipedia #pip install wikipedia
import webbrowser
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import pyaudio
#pip install PyAudio
import pyautogui #pip install pyautogui
import pvporcupine #pip3 install pvporcupine
import struct
import json
import requests
from urllib.request import urlopen
import winsound
import wolframalpha as wol #pip install wolframalpha
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wol_app_id='HVXE5X-XHPAYER849'

def readychime():
    winsound.Beep(600,300)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('Recognizing.....')
        query=r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print('Say that again please')
        return "None"
    return query




def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")#For 12 hour clock
    speak("The current time is")
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak('Today\'s date is')
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak('Good Morning User, bumblebee at your service')
    elif hour==12:
        speak('Good Noon User, bumblebee at your service')
    elif hour>=12 and hour<16:
        speak('Good Afternoon User, bumblebee at your service')
    elif hour>=16 and hour<20:
        speak('Good Evening User, bumblebee at your service')
    else:
        speak('Good Night User, bumblebee at your service')
    time_()
    date_()

def guide():
    speak('Hi my name is Bumblebee. I am a personal Assistant made by Arya Ameen.')
    speak('I am built mainly using Python and a little bit of Node J S.')
    speak('I have 15 features including, telling the time, date, greeting you.')
    speak('telling you a joke, telling you about your cpu performance, searching wikipedia.')
    speak('searching youtube, searching google, writing and showing a note, playing a song, telling you about the weather, performing arithmetic calculations, giving you definitions of words and finally taking a screenshot.')

def joke():
    speak(pyjokes.get_joke())

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery= psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)
    speak('percent')

def wikipedia_(query):
    speak('Searching...')
    temp=query
    query1=temp.replace('wikipedia','')
    result=wikipedia.summary(query1,sentences=3)
    print(result)
    speak('According to Wikipedia')
    speak(result)
    speak('do you want more information?')
    ext=TakeCommand().lower()
    if 'yes' in ext:
        speak('ok')
        sen=result
        result1=wikipedia.summary(query1,sentences=6)
        result2=result1.replace(sen,'')
        print(result2)
        speak(result2)
    
def who(query):
    speak('Searching...')
    query1=query.replace('who is','')
    result=wikipedia.summary(query1,sentences=3)
    print(result)
    speak('According to Wikipedia')
    speak(result)
    speak('do you want more information?')
    ext=TakeCommand().lower()
    if 'yes' in ext:
        speak('ok')
        sen=result
        result1=wikipedia.summary(query1,sentences=6)
        result2=result1.replace(sen,'')
        print(result2)
        speak(result2)

def screenshot():
    scrnsht= pyautogui.screenshot()
    scrnsht.save('C:/Users/Priyam/Desktop/screenshot/screenshot.png')
    speak('I took the Screenshot')

def songs():
    speak('what song should I play')
    search=TakeCommand().lower()
    speak('Searching')
    webbrowser.open('https://open.spotify.com/search/'+search)

def news_bussiness():
    try: 
        jsonObj= urlopen('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3911c23add484c119b88fc1467263bf1')
        data= json.load(jsonObj)
        i = 1
        speak('here are some top headlines from the Bussiness industry')
        print('==================TOP HEADLINES====================' + '\n')
        for item in data['articles']:
            print(str(i)+'. '+item['title']+'\n')
            print(item['description']+'\n')
            speak(item['title'])
            i += 1
        
    except Exception as e:
            print(str(e))

def nav():
    query=query.replace('where is','')
    location= query
    speak('user asked to locate'+ location)
    webbrowser.open_new_tab("https://www.google.com/maps/place"+location)

def calc():
    client=wol.Client(wol_app_id)
    index=query.lower().split().index('calculate')
    query=query.split()[index+1]
    res=client.query(''.join(query))
    answer=next(res.results).text
    print('The Answer is:'+ answer)
    speak('The Answer is'+answer)


def get_temperature(json_data):
    temp_in_celcius = json_data['main']['temp']
    return temp_in_celcius #obtains the temperature (current)

def get_weather_type(json_data):
    weather_type = json_data['weather'][0]['description']
    return weather_type #obtains the weatehr type (current)

def get_wind_speed(json_data):
    wind_speed = json_data['wind']['speed']
    return wind_speed #obtains the wind speed (current)

def get_weather_data(json_data, city):
    description_of_weather = json_data['weather'][0]['description']
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = ''
    return weather_details + ("The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} kilometres per hour".format(city, weather_type, temperature, wind_speed)) # def for weather collection

def weather(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q=vadodara&appid=0352bcdda7c83e4bb383b48e6e8a0f55&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    speak('the weather is'+weather)
    speak("the temperature is"+ f"{temperature}℃")
    speak("feels like"+ f"{feels_like}℃")




def convo():    
    while True:    
        query=TakeCommand().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak('Searching...')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            print(result)
            speak('According to Wikipedia')
            speak(result)
            speak('do you want more information?')
            ext=TakeCommand().lower()
            if 'yes' in ext:
                speak('ok')
                sen=result
                result1=wikipedia.summary(query,sentences=6)
                result2=result1.replace(sen,'')
                print(result2)
                speak(result2)
        elif 'who is' in query:
            speak('Searching...')
            query1=query.replace('who is','')
            result=wikipedia.summary(query1,sentences=3)
            print(result)
            speak('According to Wikipedia')
            speak(result)
            speak('do you want more information?')
            ext=TakeCommand().lower()
            if 'yes' in ext:
                speak('ok')
                sen=result
                result1=wikipedia.summary(query1,sentences=6)
                result2=result1.replace(sen,'')
                print(result2)
                speak(result2)
        elif 'search youtube' in query:
            speak('What should I search for?')
            search=TakeCommand().lower()
            speak('Here we go to Youtube')
            webbrowser.open('https://www.youtube.com/results?search_query='+search)
        elif 'search google' in query:
            speak('what should I search in Google?')
            search=TakeCommand().lower()
            speak('Searching')
            webbrowser.open('https://www.google.com/search?q='+search)
        elif 'cpu' in query:
            cpu()
        
        elif 'joke' in query:
            joke()

        elif 'go offline' in query or 'stop' in query or 'quit' in query:
            speak('Going offline')
            quit()
        elif 'write a note' in query:
            speak('What should I write?')
            notes=TakeCommand()
            file=open('notes.txt','w')
            speak('Should I include date and time?')
            ans=TakeCommand()
            if 'yes' in ans:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking notes')
            else:
                file.write(notes)
        elif 'show note' in query:
            speak('Showing notes')
            file=open('notes.txt','r')
            print(file.read())
            speak(file.read())
        elif 'screenshot' in query:
            screenshot()
        elif 'guide' in query or 'tour' in query:
            guide()
        elif 'bye' in query:
            break
        elif 'song' in query:
            songs()
        elif 'news' in query:
            news_bussiness()
        elif 'where is' in query:
            nav()
        elif 'calculate' in query:
            calc()
        elif 'what is' in query:
            temp=query
            client= wol.Client(wol_app_id)
            res=client.query(temp)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print('No Results')
                speak('No Results')
        elif 'weather' in query:
            weather(city='vadodara')           
        break
porcupine=None
paud=None
audio_stream=None

try:
    access_key="T1JXDzaRKkRbdx7A2hRbAw2tbWYwDUTG0ituNYgfOy/evSrLgyvGKA=="
    keyword_path='F:\\Personal Project\\heybumblebeezip\\hey-bumblebee_en_windows_v2_1_0.ppn'
    porcupine = pvporcupine.create(access_key, keywords=[ 'bumblebee']) 
    paud=pyaudio.PyAudio()
    audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
    while True:
        keyword=audio_stream.read(porcupine.frame_length)
        keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
        keyword_index=porcupine.process(keyword)
        if keyword_index>=0:
            readychime()
            convo()
            

finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if paud is not None:
        paud.terminate()