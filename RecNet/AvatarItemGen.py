import json
import ProgramUtils
import data
import sys
import requests


name = f"{__name__}.py"

def gen(writeFile: str):
    print(f"[{name}] Downloadimg")
    sk = requests.request("GET", f"{data.dataUrl}AvatarItems.json")
    if sk.status_code != 200:
        print(f"ERROR HTTP: {sk.status_code}")
        input()
        sys.exit()
    try:
        sk = sk.json()
    except:
        print(f"ERROR JSON: 0001")
        input()
        sys.exit()

    with open(writeFile, "w") as f:
        json.dump(sk, f, indent=2)

    print(f"[{name}] Done")