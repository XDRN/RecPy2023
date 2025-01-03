import subprocess
import socket
import datetime

def getVersion():
    return 0.1

def getName():
    return "Rec.py2023"


def clearScreen():
    subprocess.run("cls", shell=True)

def getCurrentTime():
  now = datetime.datetime.now()
  currentTime = now.isoformat()
  return currentTime

def setConsoleTitle(Text):
    subprocess.run(f"title {Text}", shell=True)