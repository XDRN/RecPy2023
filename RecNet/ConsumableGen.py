import json
import data
import sys
import requests

import ProgramUtils

name = f"{__name__}.py"

def gen(writeFile: str):
    print(f"[{name}] Generating")
    sk = requests.request("GET", f"{data.dataUrl}ConsumableCollectionRuntimeConfig.json")
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
    GenericConsumables = sk["GenericConsumables"]
    HairDyeConsumables = sk["HairDyeConsumables"]
    CouponConsumables = sk["CouponConsumables"]
    HeadPotionConsumables = sk["HeadPotionConsumables"]


    Consumables = []

    num = 1
           
    for GenericConsumable in GenericConsumables:
        Consumable1 = {
            "Ids":[num],
            "CreatedAts":[ProgramUtils.getCurrentTime()],
            "ConsumableItemDesc":GenericConsumable["ConsumableItemDesc"],
            "Count":4294967295,
            "InitialCount":4294967295,
            "IsActive":False,
            "ActiveDurationMinutes":None,
            "IsTransferable":False
        }
        Consumables.append(Consumable1)
        num += 1

    for HairDyeConsumable in HairDyeConsumables:
        Consumable1 = {
            "Ids":[num],
            "CreatedAts":[ProgramUtils.getCurrentTime()],
            "ConsumableItemDesc":HairDyeConsumable["ConsumableItemDesc"],
            "Count":4294967295,
            "InitialCount":4294967295,
            "IsActive":False,
            "ActiveDurationMinutes":None,
            "IsTransferable":False
        }
        Consumables.append(Consumable1)
        num += 1

    for CouponConsumable in CouponConsumables:
        Consumable1 = {
            "Ids":[num],
            "CreatedAts":[ProgramUtils.getCurrentTime()],
            "ConsumableItemDesc":CouponConsumable["ConsumableItemDesc"],
            "Count":4294967295,
            "InitialCount":4294967295,
            "IsActive":False,
            "ActiveDurationMinutes":None,
            "IsTransferable":False
        }
        Consumables.append(Consumable1)
        num += 1

    for HeadPotionConsumable in HeadPotionConsumables:
        Consumable1 = {
            "Ids":[num],
            "CreatedAts":[ProgramUtils.getCurrentTime()],
            "ConsumableItemDesc":HeadPotionConsumable["ConsumableItemDesc"],
            "Count":4294967295,
            "InitialCount":4294967295,
            "IsActive":False,
            "ActiveDurationMinutes":None,
            "IsTransferable":False
        }
        Consumables.append(Consumable1)
        num += 1

    with open(writeFile, "w") as f:
        json.dump(Consumables, f, indent=2)

    print(f"[{name}] Done")