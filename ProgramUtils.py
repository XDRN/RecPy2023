import subprocess
import socket
import datetime

Version = "0.1-keepsake-testing"


def clearScreen():
    subprocess.run("cls", shell=True)

def getCurrentTime():
  now = datetime.datetime.now()
  currentTime = now.isoformat()
  return currentTime

def setConsoleTitle(Text):
    subprocess.run(f"title {Text}", shell=True)
