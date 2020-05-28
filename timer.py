import win32event
from time import sleep
from win32event import CreateWaitableTimer
from win32event import SetWaitableTimer
from win32event import WaitForSingleObject
import sys
import pyautogui as py
from datetime import datetime as dt
import datetime
from datetime import timedelta
import os



def wakeup(minutes):
    os.system('powercfg /SETACVALUEINDEX SCHEME_CURRENT SUB_NONE CONSOLELOCK 0')
    minutes = int(minutes)
    handle = CreateWaitableTimer(None, True, 'Wake up')
    dt = -10000000 * minutes * 60 # Convert to seconds.
    SetWaitableTimer(handle, dt, 0, None, None, True)
    rc = WaitForSingleObject(handle, 1000 * (minutes + 1) * 60) # 11 s.
    
    os.system('powercfg /SETACVALUEINDEX SCHEME_CURRENT SUB_NONE CONSOLELOCK 1')

