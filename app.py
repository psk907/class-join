import pyautogui as pyg  # stuff with this isnt working great
import datetime
import json
import webbrowser
import time
import click


def get_day_code(weekday):
    if weekday == 0:
        return "mon"
    if weekday == 1:
        return "tues"
    if weekday == 2:
        return "wed"
    if weekday == 3:
        return "thurs"
    if weekday == 4:
        return "fri"
    if weekday == 5:
        return "sat"
    if weekday == 6:
        return "sun"


def get_period(current_hour):
    if(current_hour == 9):
        return 0
    if(current_hour == 10):
        return 1
    if(current_hour == 11):
        return 2
    if(current_hour == 12):
        return 3
    if(current_hour == 14):
        return 4
    if(current_hour == 15):
        return 5
    return (-1)


def join_impartus_class():
    webbrowser.open("https://a.impartus.com/ilc/#/home", new=2, autoraise=True)
    time.sleep(2)
    impartus_login_btn = pyg.locateCenterOnScreen("assets/impartus_login.png")
    if impartus_login_btn != None:
        pyg.moveTo(impartus_login_btn)
        pyg.click()
        print("Login manually")
        # exit()
    time.sleep(10)
    impartus_join_btn = pyg.locateCenterOnScreen("assets/impartus_join.png")
    print(impartus_join_btn)
    pyg.moveTo(impartus_join_btn)
    pyg.click()


def join_zoom_class(link):
    webbrowser.open(link, new=2, autoraise=False)


data = dict()
try:
    f = open('data.json',)
    # returns JSON object as a dictionary
    data = json.load(f)
except:
    print("File not found")

current_dt = datetime.datetime.now()
current_weekday = datetime.date.today().weekday()
current_time = current_dt.time()
current_hour = current_time.hour
print(current_time.hour)
current_period = get_period(current_hour)
if(current_period == -1):
    print("No class")
    exit()
current_link = data['links'][get_day_code(
    current_weekday)][current_period]
print(current_link)
if(current_link == "none"):
    print("No class")

elif current_link == "impartus":
    join_impartus_class()
elif current_link == "tbd":
    print("No link")
else:
    join_zoom_class(current_link)
    print("Joined on zoom")
