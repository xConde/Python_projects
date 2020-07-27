import time
from datetime import datetime as dt
import os
import ctypes

"""
Stop_Discord: Block_Applications.py
Stops user interaction during the period of 0600 to 1700 (6AM-5PM) to programs specified in program_list
to encourage productivity.

"""

program_list = ["Discord.exe", "steam.exe"]


def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    for i in range(len(r)):
        if name in r[i]:
            return True
    return False


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 6) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Focus on work.")
        for apps in program_list:
            if getTasks(apps):
                os.system('taskkill /f /im ' + apps)
                ctypes.windll.user32.MessageBoxW(0, 'Get back to work!', 'Alert!', 0)
    else:
        print("Time to relax.")
    time.sleep(10)
