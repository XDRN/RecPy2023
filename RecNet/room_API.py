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
    rooms = []

#temp = {
#    "Accessibility":1,
#    "CloningAllowed":False,
#    "CreatedAt":ProgramUtils.getCurrentTime(),
#    "CreatorAccountId":playerId,
#    "CustomWarning":"",
#    "DataBlob":None,
#    "Description":"An introductory tour of Rec Room!",
#    "DisableMicAutoMute":False,
#    "DisableRoomComments":False,
#    "EncryptVoiceChat":False,
#    "ImageName":"DefaultRoomImage.jpg",
#    "IsDeveloperOwned":True,
#    "IsDorm":False,
#    "IsRRO":True,
#    "LoadScreenLocked":False,
#    "LoadScreens":[],
#    "MaxPlayerCalculationMode":1,
#    "MaxPlayers":1,
#    "MinLevel":0,
#    "Name":"Orientation",
#    "PromoExternalContent":[],
#    "PromoImages":[],
#    "Roles":[
#        {
#            "AccountId":playerId,
#            "InvitedRole":0,
#            "Role":255
#        }
#    ],
#    "RoomId":2,
#    "State":0,
#    "Stats":{
#        "CheerCount":0,
#        "FavoriteCount":0,
#        "VisitCount":0,
#        "VisitorCount":0
#    },
#    "SubRooms":[
#        {
#            "Accessibility":1,
#            "CurrentSave":{
#                "CreatedAt":ProgramUtils.getCurrentTime(),
#                "DataBlob":"",
#                "Description":"",
#                "SavedByAccountId":playerId,
#                "SavedOnDeviceClass":0,
#                "SavedOnPlatform":0,
#                "SubRoomDataSaveId":0,
#            },
#            "IsSandbox":True,
#            "MaxPlayers":1,
#            "Name":"Home",
#            "RoomId":2,
#            "SubRoomId":2,
#            "UnitySceneId":"c79709d8-a31b-48aa-9eb8-cc31ba9505e8"
#        }
#    ],
#    "SupportsJuniors":True,
#    "SupportsLevelVoting":False,
#    "SupportsMobile":True,
#    "SupportsQuest2":True,
#    "SupportsScreens":True,
#    "SupportsTeleportVR":True,
#    "SupportsVRLow":True,
#    "SupportsWalkVR":True,
#    "Tags":[],
#    "Version":0,
#    "WarningMask":0
#}


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
    print(f"[{name}] Done (Loaded Rooms)")

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