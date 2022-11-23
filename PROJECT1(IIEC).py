from subprocess import getoutput as system
import pyttsx3
from datetime import date
import speech_recognition as sr

def tasks(user):
    if "chrome" in user or "browser" in user:
        system("chrome")
    if "word" in user:
        system("winword")
    if "excel" in user:
        system("excel")
    if "power" in user or "ppt" in user:
        system("powerpnt")
    if "notepad" in user or "text" in user:
        system("notepad")
    if "media player" in user or "player" in user:
        print("ok ")
        print("what should open vlc or windows media player")
        ser = input()
        if "vlc" in ser:
            system("vlc")
        if "windows" in ser:
            system("wmplayer")
    if "vlc" in user:
        system("vlc")
    if "windows" in user:
        system("wmplayer")
    if "office" in user:
        print("")
        print("i can able to open word, powerpoint and excel for you")
        ser = input()
        if "word" in ser:
            system("winword")
        if "excel" in ser:
            system("excel")
        if "power" in ser or "ppt" in ser:
            system("powerpnt")
    if "mail" in user:
        system("chrome gmail.com")
    if "social" in user or "social media" in user:
        print()
        print("i can open whatsApp, facebook, linkedln and twitter for u monik")
        ser = input()
        if "whatsapp" in ser:
            system("whatsapp")
        if "facebook" in ser:
            system("chrome facebook.com")
        if "linkedln" in ser:
            system("chrome linkedin.com/feed/")
        if "twitter" in ser:
            system("chrome twitter.com")
    if "whatsapp" in user:
        system("whatsapp")
    if "facebook" in user:
        system("chrome facebook.com")
    if "linkedln" in user:
        system("chrome linkedin.com/feed/")
    if "twitter" in user:
        system("chrome twitter.com")
    else:


current = str(date.today())
year, month, day = (int(i) for i in current.split("-"))
top = date(year, month, day).strftime("%A")

pyttsx3.speak("hi, welcome Monik. Hope u are having a good" + top)
print('''
       Jarvis at you service
    --------------------------

I am a menu driven program 
what can i do for you''',end="\n\n")

# how about use subprocess.getoutput instead of os.system

while True:
    query = input()
    query = query.lower()
    if "don't" in query or "do not" in query or "don" in query:
        findDontIndex = query.find("do")
        doUser = query[findDontIndex:]
        query = query[:findDontIndex]
        if ("run" in user or "execute" in user or "launch" in user or "open" in user) and (
                "don't" not in user or "do not" not in user or "don" not in user):
           tasks()
        if "but" in doUser:
            findAndIndex = doUser.find("but")
            douser = doUser[findAndIndex:]
            if "run" in douser or "execute" in douser or "launch" in douser or "open" in douser:
                tasks(douser)
        if "instead" in doUser:
            findAndIndex = doUser.find("instead")
            douser = doUser[findAndIndex:]
            if "run" in douser or "execute" in douser or "launch" in douser or "open" in douser:
               tasks(douser)
    elif ("run" in query or "execute" in query or "launch" in query or "open" in query) and ("chrome" in query or "browser" in query or "word" in query or "excel" in query or "power" in query or "ppt" in query or "notepad" in query or "text" in query or "media player" in query or "player" in query or "vlc" in query or "windows" in query or "office" in query or "twitter" in query or "linkedln" in query or "facebook" in query or "whatsapp" in query or "social" in query or "social media" in query or "mail" in query):
        tasks(query)
    elif "option" in query or "menu" in query:
        pyttsx3.speak("given below are the task which i can perform")
        print('''
Following are the task which i can perform-
    1.chrome
    2.social media
      whatsapp
      facebook
      linkedln
      twitter
    3.E-mail
    4.MS-office
      word
      powerpoint
      excel
    5.notepad
    6.media player
      vlc
      windows media player''')

    elif "bye" in query or "exit" in query or "quit" in query or "close" in query:
        print("\nhope u enjoyed my service")

        break
    else:
        pyttsx3.speak("I am not able to help with that monik, but i can help with the following")
        print("I am not able to help with that monik, but i can help with the following")
        print('''
Following are the task which i can perform-
    1.chrome
    2.social media
      whatsapp
      facebook
      linkedln
      twitter
    3.E-mail
    4.MS-office
      word
      powerpoint
      excel
    5.notepad
    6.media player
      vlc
      windows media player''',end="\n\n")

    print("-------------------------------------------",end="\n\n")
    print("what else can i do for you", end="\n\n")
