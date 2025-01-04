import colorama
from colorama import Fore
colorama.init()
print(f"{Fore.MAGENTA} Starting")
#import api, notify, Matchmaking
import threading
import ProgramUtils

#threading.Thread(target=notify.run).start()
#threading.Thread(target=Matchmaking.run).start()
#api.run()

def mainMenu():
    print(f"Rec.py2023 - Open source Old RecRoom server software for 20223. (Version:{ProgramUtils.getVersion()})\nMade and provided by EggRecRoom\nDownload source code here: null")
    print(f"\n{Fore.RED}! Some Rooms Wont Load !{Fore.MAGENTA}")
    print(f"\n\n(1) Change Settings\n(2) Modify Profile\n(3) Start Server")
    ufgtftftfty = input()
    _input = int(ufgtftftfty)
    if _input == 1:
        pass
    elif _input == 2:
        pass
    elif _input == 3:
        ProgramUtils.clearScreen()
        print("Starting")
        import api, notify, Matchmaking, Cdn
        threading.Thread(target=notify.run).start()
        threading.Thread(target=Matchmaking.run).start()
        threading.Thread(target=Cdn.run).start()
        api.run()


ProgramUtils.clearScreen()
mainMenu()