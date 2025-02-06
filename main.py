import colorama
from colorama import Fore
colorama.init()
print(f"{Fore.MAGENTA}Starting")
import threading
import ProgramUtils
import os
import data

if not os.path.exists(data.saveDataPath):
    import SetUp
    ProgramUtils.clearScreen()
    SetUp.setUp()

def mainMenu():
    print(f"Rec.py2023 - Open source old RecRoom server for 2023.\nMade by EggRecRoom")
    print(f"\n{Fore.RED}! Some Rooms Wont Load !{Fore.MAGENTA}")
    print(f"\n\n1. Modify Profile\n2. Start Server")
    ufgtftftfty = input()
    _input = int(ufgtftftfty)
    match _input:
        case 2:
            ProgramUtils.clearScreen()
            print("Starting")
            import api, notify, Matchmaking
            threading.Thread(target=notify.run).start()
            threading.Thread(target=Matchmaking.run).start()
            api.run()
        case _:
            ProgramUtils.clearScreen()
            mainMenu()


ProgramUtils.clearScreen()
mainMenu()