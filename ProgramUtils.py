import subprocess
import socket
import datetime

Version = "WebSocket Test 0.1"

Branch = "Test-WebSockets"


def clearScreen():
    subprocess.run("cls", shell=True)

def getCurrentTime():
  now = datetime.datetime.now()
  currentTime = now.isoformat()
  return currentTime

def setConsoleTitle(Text):
    subprocess.run(f"title {Text}", shell=True)