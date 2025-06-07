# invention_manager.py
from datetime import datetime
import data
import random

def getmyPlayerID():
    with open(f"{data.saveDataPath}Profile\\userid.txt") as f:
        try:
            userid = int(f.read())
        except:
            userid = random.randint(10000,9999999999)
    return userid

 #TODO: Store in file so inventions save when server restarts
invention_storage = []

def generate_invention_response(data):
    now = datetime.utcnow().isoformat() + "Z"
    invention_id = random.randint(5000000, 5999999)

    invention = {
        "InventionId": invention_id,
        "ReplicationId": "",
        "CreatorPlayerId": getmyPlayerID(),
        "Name": data.get("name", "Unnamed Invention"),
        "Description": data.get("description", ""),
        "ImageName": data.get("imageName", "placeholder.png"),
        "CurrentVersionNumber": 1,
        "IsPublished": False,
        "AllowTrial": False,
        "ModifiedAt": now,
        "CreatedAt": now,
        "NumPlayersHaveUsedInRoom": 0,
        "NumDownloads": 0,
        "CheerCount": 0,
        "CreatorPermission": 100,
        "GeneralPermission": 100
    }

    invention_storage.append(invention)

    return {
        "Status": 0,
        "Invention": invention,
        "InventionVersion": {
            "InventionId": invention_id,
            "ReplicationId": "",
            "VersionNumber": 1,
            "InstantiationCost": data.get("instantiationCost", 0),
            "LightsCost": data.get("lightsCost", 0),
            "BlobName": data.get("inventionDataFilename", "")
        }
    }

def get_all_inventions():
    return invention_storage

def get_invention_by_id(invention_id):
    for invention in invention_storage:
        if invention["InventionId"] == invention_id:
            return [invention]


