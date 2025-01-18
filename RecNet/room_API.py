import random
import ProgramUtils
import json
import data
import random
import sys
import requests

from RecNet import player_API
name = f"{__name__}.py"
playerId = player_API.getmyPlayer()["accountId"]
createdAt = ProgramUtils.getCurrentTime()

def init():
    global rooms
    global unityAssets
    rooms = []
    unityAssets = []

def loadRooms():
    print(f"[{name}] Downloading Main Rooms")
    Rooms2 = requests.request("GET", f"{data.dataUrl}AGRoomRuntimeConfig.json")
    if Rooms2.status_code != 200:
        print(f"ERROR HTTP: {Rooms2.status_code}")
        input()
        sys.exit()
    try:
        Rooms2 = Rooms2.json()
    except:
        print(f"ERROR JSON: 0001")
    num = 1
    subnum = 1
    Rooms2 = Rooms2["Rooms"]
    for room in Rooms2:
        SubRooms = []
        IsDorm = False
        if room["ReplicationId"] == "68251132-5662-5c34-08b1-4a830a27955b":
            IsDorm = True
        temp = {
            "Accessibility":1,
            "CloningAllowed":False,
            "CreatedAt":ProgramUtils.getCurrentTime(),
            "CreatorAccountId":1,
            "CustomWarning":"",
            "DataBlob":None,
            "Description":room["Description"],
            "DisableMicAutoMute":False,
            "DisableRoomComments":False,
            "EncryptVoiceChat":False,
            "ImageName":"DefaultRoomImage.jpg",
            "IsDeveloperOwned":True,
            "IsDorm":IsDorm,
            "IsRRO":True,
            "LoadScreenLocked":False,
            "LoadScreens":[],
            "MaxPlayerCalculationMode":1,
            "MaxPlayers":1,
            "MinLevel":0,
            "Name":room["Name"],
            "PromoExternalContent":[],
            "PromoImages":[],
            "Roles":[
                {
                    "AccountId":1,
                    "InvitedRole":0,
                    "Role":255
                },
                {
                    "AccountId":playerId,
                    "InvitedRole":0,
                    "Role":30
                }
            ],
            "RoomId":num,
            "State":0,
            "Stats":{
                "CheerCount":0,
                "FavoriteCount":0,
                "VisitCount":0,
                "VisitorCount":0
            },
            "SupportsJuniors":True,
            "SupportsLevelVoting":False,
            "SupportsMobile":True,
            "SupportsQuest2":True,
            "SupportsScreens":True,
            "SupportsTeleportVR":True,
            "SupportsVRLow":True,
            "SupportsWalkVR":True,
            "Tags":[],
            "Version":0,
            "WarningMask":0
        }
        for x in room["Scenes"]:
            temp2 = {
                "Accessibility":1,
                "CurrentSave":None,
                "IsSandbox":x["IsSandbox"],
                "MaxPlayers":x["MaxPlayers"],
                "Name":x["Name"],
                "RoomId":num,
                "SubRoomId":subnum,
                "UnitySceneId":x["RoomSceneLocationId"]
            }
            SubRooms.append(temp2)
            subnum += 1
        temp.update({
            "SubRooms": SubRooms
        })
        num += 1
        rooms.append(temp)
    print(f"[{name}] Downloading Rooms")
    Rooms2 = requests.request("GET", f"{data.dataUrl}Rooms.json")
    if Rooms2.status_code != 200:
        print(f"ERROR HTTP: {Rooms2.status_code}")
        input()
        sys.exit()
    try:
        Rooms2 = Rooms2.json()
    except:
        print(f"ERROR JSON: 0001")
    for room in Rooms2:
        SubRooms = []
        temp = {
            "Accessibility":1,
            "CloningAllowed":False,
            "CreatedAt":ProgramUtils.getCurrentTime(),
            "CreatorAccountId":1,
            "CustomWarning":"",
            "DataBlob":None,
            "Description":room["BHPRHUDFBWZCEIJFVQHG"],
            "DisableMicAutoMute":False,
            "DisableRoomComments":False,
            "EncryptVoiceChat":False,
            "ImageName":"DefaultRoomImage.jpg",
            "IsDeveloperOwned":True,
            "IsDorm":IsDorm,
            "IsRRO":True,
            "LoadScreenLocked":False,
            "LoadScreens":[],
            "MaxPlayerCalculationMode":1,
            "MaxPlayers":1,
            "MinLevel":0,
            "Name":room["CIVPEMESQAIUBLZHXUNA"],
            "PromoExternalContent":[],
            "PromoImages":[],
            "Roles":[
                {
                    "AccountId":1,
                    "InvitedRole":0,
                    "Role":255
                },
                {
                    "AccountId":playerId,
                    "InvitedRole":0,
                    "Role":30
                }
            ],
            "RoomId":num,
            "State":0,
            "Stats":{
                "CheerCount":0,
                "FavoriteCount":0,
                "VisitCount":0,
                "VisitorCount":0
            },
            "SupportsJuniors":True,
            "SupportsLevelVoting":False,
            "SupportsMobile":True,
            "SupportsQuest2":True,
            "SupportsScreens":True,
            "SupportsTeleportVR":True,
            "SupportsVRLow":True,
            "SupportsWalkVR":True,
            "Tags":[],
            "Version":0,
            "WarningMask":0
        }
        for x in room["NLZGBCXTQDCXNQYNWMSZ"]:
            temp2 = {
                "Accessibility":1,
                "CurrentSave":{
                    "SubRoomDataSaveId": subnum,
                    "SubRoomId": subnum,
                    "DataBlob": x["GKDQCTIXPBRUUTAORXFX"],
                    "SavedByAccountId": 1,
                    "SavedOnPlatform": None,
                    "SavedOnDeviceClass": None,
                    "Description": None,
                    "CreatedAt": ProgramUtils.getCurrentTime(),
                    "UnityAssetId": x["UnityAssetId"]
                },
                "IsSandbox":False,
                "MaxPlayers":x["DXLCSNGZJQYZCJCCHKAQ"],
                "Name":x["XABBIXTJPMRVUDZURJSQ"],
                "RoomId":num,
                "SubRoomId":subnum,
                "UnitySceneId":x["TCUGHHWOAWGHMQYQAZNY"]
            }
            SubRooms.append(temp2)
            subnum += 1
        temp.update({
            "SubRooms": SubRooms
        })
        num += 1
        rooms.append(temp)
    print(f"[{name}] Done (Loaded Rooms)")

def loadUnityAssets():
    global unityAssets
    print(f"[{name}] Downloading Unity Assets")
    UnityAssets = requests.request("GET", f"{data.dataUrl}UnityAssets.json")
    if UnityAssets.status_code != 200:
        print(f"ERROR HTTP: {UnityAssets.status_code}")
        input()
        sys.exit()
    try:
        UnityAssets = UnityAssets.json()
    except:
        print(f"ERROR JSON: 0001")
    unityAssets = UnityAssets
    print(f"[{name}] Done (Loaded Unity Assets)")

def findRoom(RoomName: str):
    for room in rooms:
        if room["Name"].lower() == RoomName.lower():
            return room
    return

def findRoomId(Id: int):
    for room in rooms:
        if room["RoomId"] == Id:
            return room
    return

def findUnityAsset(GUID: str):
    for room in unityAssets:
        if room["UnityAssetId"] == GUID:
            return room
    return