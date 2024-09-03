#AI MADE BY PARAMESH KUMAR

import pyttsx3 as ai
import datetime
import pywhatkit

engine = ai.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voices",voice[0])


def say(audio):
    engine.say(audio)
    engine.runAndWait()


say("PLEASE ENTER YOUR PASSWORD :")
password=str(input("PLEASE ENTER THE PASSWORD : "))


now = datetime.datetime.now()
current_time = int(now.strftime("%H"))


def crt_user():
    if(password == "8"):
        say("HAI BOSS")
    elif(password=="4"):
        say("HAI MISSES BOSS")
    else:
        say("DAM IT . WHO ARE YOU . WHAT ARE YOU DOING HERE? . GET LOST.")
        exit() 


def wish():
    if(current_time>=0 and current_time<=11 and password=="4"): 
        say("GOOD MORNING. I AM JARVIS , WHAT CAN I DO FOR YOU?.")
    elif(current_time>11 and current_time<=16):
        say("GOOD AFTERNOON I AM JARVIS , WHAT CAN I DO FOR YOU?.")
    elif(current_time>16):
        say("GOOD EVENING , I AM JARVIS , WHAT CAN I DO FOR YOU?.")
    else:
        say("Try Again.")
        
    """elif(current_time>=0 and current_time<=11 and password=="8"):
        say("GOOD MORNING I AM JARVIS , WHAT CAN I DO FOR YOU?")
    elif(current_time>11 and current_time<=16 and password=="8"):
        say("GOOD AFTERNOON I AM JARVIS , WHAT CAN I DO FOR YOU?")
    elif(current_time>11 and current_time<=16 and password=="8"):
        say("GOOD EVENING I AM JARVIS , WHAT CAN I DO FOR YOU?")"""

crt_user()
wish()


def youtube(Serach):
    pywhatkit.playonyt(Serach)
def Google(Search):
    pywhatkit.search(Search)


Search=str(input("Enter To Search : "))

if("You Tube" in Search):
    print("Working On It....")
    youtube(Search)
elif("you tube" in Search):
    print("Working On It....")
    youtube(Search)
elif("Youtube" in Search):
    print("Working On It....")
    youtube(Search)
elif("youtube" in Search):
    print("Working On It....")
    youtube(Search)
elif("YOU TUBE" in Search):
    print("Working On It....")
    youtube(Search)
elif("YOUTUBE" in Search):
    print("Working On It....")
    youtube(Search)
elif("YT" in Search):
    print("Working On It....")
    youtube(Search)
elif("yt" in Search):
    print("Working On It....")
    youtube(Search)
else:
    print("Working On it....")
    Google(Search)

