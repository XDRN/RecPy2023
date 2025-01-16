import random
import ProgramUtils
import data

createdAt = ProgramUtils.getCurrentTime()


def getmyPlayer():
    with open(f"{data.saveDataPath}Profile\\username.txt") as f:
        username = f.read()
    with open(f"{data.saveDataPath}Profile\\userid.txt") as f:
        try:
            userid = int(f.read())
        except:
            userid = random.randint(10000,9999999999)
    return {
        "accountId": userid,
        "username": username,
        "displayName": username,
        "profileImage": "3vltmrmtk3vjyyqkqeln9hdnb.jpg",
        "bannerImage": "3vltmrmtk3vjyyqkqeln9hdnb.jpg",
        "isJunior": False,
        "platforms": 1,
        "personalPronouns": 0,
        "identityFlags": 0,
        "createdAt": createdAt,
        "isMetaPlatformBlocked": False
    }

def getcachedlogins(platform: int,PlatformId: str):
    with open(f"{data.saveDataPath}Profile\\userid.txt") as f:
        try:
            userid = int(f.read())
        except:
            userid = random.randint(10000,9999999999)
    return [{
        "platform": platform,
        "platformId": PlatformId,
        "accountId": userid,
        "lastLoginTime": createdAt,
        "requirePassword": False,
    }]