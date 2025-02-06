import json
import data
import sys
import requests

name = f"{__name__}.py"

def gen(writeFile: str):
    print(f"[{name}] Generating")
    sk = requests.request("GET", f"{data.dataUrl}EquipmentWardrobeRuntimeConfig.json")
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
    toolSkinMaps = sk["toolSkinMaps"]

    skinlist = []

    for toolSkinMap in toolSkinMaps:
        equipment = toolSkinMap["equipment"]
        skins = toolSkinMap["skins"]
        for skin in skins:
            FriendlyNameSkinAssetName = str(skin["skinAssetName"])
            FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("_Skin", "")
            FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("Skin", "")
            FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("_", " ")
            FriendlyName = f"{FriendlyNameSkinAssetName}"
            newskin1 = {
                'PrefabName': equipment["prefabName"], 
                'ModificationGuid': skin["skinGuid"], 
                'Favorited': False, 
                'PlatformMask': -1, 
                'FriendlyName': FriendlyName, 
                'Tooltip': '', 
                'Rarity': 50, 
                'ThumbnailImageName': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
            }
            skinlist.append(newskin1)

    with open(writeFile, "w") as f:
        json.dump(skinlist, f, indent=2)

    print(f"[{name}] Done")

def getByPrefabNameAndModificationGuid(PrefabName: str, ModificationGuid: str):
    pass