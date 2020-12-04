import pyttsx3 #pip install pyttsx3
import os
import sys
import psutil
import datetime
import speech_recognition as sr
import wikipedia  
import smtplib
import webbrowser as wb
import pyautogui
import pyjokes
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    speak("the current time is")
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
def date():
    speak("the current date is")
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("Welcome back sir!")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
           speak("GOOD MORNING")
    elif hour>=12 and hour<18:
         speak("GOOD AFTERNOON")
    elif hour>=18 and hour<24 :
          speak("GOOD EVENING")
    else:
          speak("GOOD NIGHT")
    speak("JARVIS AT YOUR SERVICE . PLEASE TELL ME HOW CAN I HELP YOU")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as  source :
        print("Lisening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising.....")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("I do not understand!")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('codechef1408@gmail.com','jagrati@1408')
    server.sendmail('codechef1408@gmail.com',to,content)
    server.close()
def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\HP\\Pictures\\Screenshots\\ss.png")
def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_jokes())



if __name__ == "__main__":
     wishme()
     while True:
        query=takeCommand().lower()
        if 'time'in query:
             time()
        elif 'date' in query:
            date()
        elif 'offline' in query:
              quit()
        elif 'wikipedia' in query:
             speak("Searching....")
             query= query.replace("wikipedia","")
             result=wikipedia.summary(query,sentences=2)
             print(result)
             speak(result)
        elif 'send email' in query:
            try:
                  speak("What should i email")
                  content=takeCommand()
                  to='janerockz14@gmail.com'
                  sendEmail(to,content)
                  speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif 'search in browser' in query:
            speak("What should i search ?")
            search=takeCommand().lower()
            wb.open_new_tab('https://www.'+search+'.com')
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play song'in query:
            songs_dir="C:\\Users\HP\Desktop\jagrati\O"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[2]))
        elif 'remember' in query:
             speak("what should i remember?")
             data=takeCommand()
             speak("you said me to remember that"+data)
             remember=open('data.txt','w')
             remember.write(data)
             remember.close()
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("you said me to remember that"+remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif  'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
             
        



               
              
        
        
    
