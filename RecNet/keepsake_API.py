import random
import ProgramUtils
import json
import data
import random
import sys
import requests

from uuid import uuid4
from RecNet import player_API

playerId = player_API.getmyPlayer()["accountId"]

def init():
    global keepsake_data
    keepsake_data = []

def remove_keepsake(Keepsake_id :str):
    global keepsake_data
    for keepsake in keepsake_data:
        if keepsake["KeepsakeInstanceId"] == Keepsake_id:
            keepsake_data.remove(keepsake)
    return

def find_keepsake_data(RoomId):
    roomlist = []
    for keepsake in keepsake_data:
        if keepsake["RoomId"] == RoomId:
            roomlist.append(keepsake)
    return roomlist.append( {
            "KeepsakeInstanceId": str(uuid4()),
            "PlacedByAccountId": playerId,
            "KeepsakeCategoryConfigId": 0,
            "RoomId": 62,
            "SubRoomId": 74
        })

def add_keepsake_data(roomid, subroomid, keepsake_type):
    global keepsake_data
    temp_id = str(uuid4())
    keepsake_data.append(
        {
            "KeepsakeInstanceId": temp_id,
            "PlacedByAccountId": playerId,
            "KeepsakeCategoryConfigId": keepsake_type,
            "RoomId": roomid,
            "SubRoomId": subroomid
        }
    )
    return temp_id