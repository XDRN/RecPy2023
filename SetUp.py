import os
import data
import json
import requests
import random
import sys

from RecNet import AvatarItemGen, Skins, ConsumableGen

import ProgramUtils

def setUp():
    print("Setting up... (May take a minute to download everything.)")
    os.mkdir(f"{data.saveDataPath}")
    os.mkdir(f"{data.saveDataPath}Profile")
    os.mkdir(f"{data.saveDataPath}Profile\\avatarSaved")
    os.mkdir(f"{data.saveDataPath}img")
    AvatarItemGen.gen("NotUsed", f"{data.saveDataPath}AvatarItems.json")
    Skins.gen(f"{data.saveDataPath}Equipments.json")
    ConsumableGen.gen(f"{data.saveDataPath}Consumables.json")
    gameconfigs = requests.request("GET", f"{data.dataUrl}gameconfigs.json")
    if gameconfigs.status_code != 200:
        print(f"ERROR HTTP: {gameconfigs.status_code} on gameconfigs")
        input()
        sys.exit()
    try:
        gameconfigs = gameconfigs.json()
    except:
        print(f"ERROR JSON: 0001 on gameconfigs")
        input()
        sys.exit()
    with open(f"{data.saveDataPath}gameconfigs.json", "w") as f:
        json.dump(gameconfigs, f, indent=2)
    with open(f"{data.saveDataPath}playersettings.json", "w") as f:
        json.dump([], f, indent=2)
    playerId = random.randint(100, 9999999)
    name = f"RecPy#{playerId}"
    profileimageUrl = f"{data.dataUrl}ewqwqddwqwqddq.png"
    avatar = {
        "OutfitSelections": "a994fc19-974e-444e-ae9e-c2f6c32432bb,,1;31bb82db-cd30-4988-a8bf-3ce55a12a4c9,db-JiDmRhUKX69weDLiHsQ,0;9bf75b23-84e9-436b-bbb8-4180ccd86b94,,0;022ce375-ed02-479d-b87d-9d72d126bbd4,dpfTnOvsrUePTVs0XZD9qQ,gOt7BYXvw0uUS-U53KThAA,,1",
        "OutfitSelectionsV2": "{\"selections\":[{\"PrefabGuid\":\"a994fc19-974e-444e-ae9e-c2f6c32432bb\",\"CombinationGuid\":\"\",\"BodyPart\":1,\"UgcOutfitData\":{\"BaseAvatarItemColor\":{\"r\":0.0,\"g\":0.0,\"b\":0.0,\"a\":0.0},\"CustomAvatarItemId\":\"\"}},{\"PrefabGuid\":\"31bb82db-cd30-4988-a8bf-3ce55a12a4c9\",\"CombinationGuid\":\"db-JiDmRhUKX69weDLiHsQ\",\"BodyPart\":0,\"UgcOutfitData\":{\"BaseAvatarItemColor\":{\"r\":0.0,\"g\":0.0,\"b\":0.0,\"a\":0.0},\"CustomAvatarItemId\":\"\"}},{\"PrefabGuid\":\"9bf75b23-84e9-436b-bbb8-4180ccd86b94\",\"CombinationGuid\":\"\",\"BodyPart\":0,\"UgcOutfitData\":{\"BaseAvatarItemColor\":{\"r\":0.0,\"g\":0.0,\"b\":0.0,\"a\":0.0},\"CustomAvatarItemId\":\"\"}},{\"PrefabGuid\":\"022ce375-ed02-479d-b87d-9d72d126bbd4\",\"CombinationGuid\":\"dpfTnOvsrUePTVs0XZD9qQ,gOt7BYXvw0uUS-U53KThAA,\",\"BodyPart\":1,\"UgcOutfitData\":{\"BaseAvatarItemColor\":{\"r\":0.0,\"g\":0.0,\"b\":0.0,\"a\":0.0},\"CustomAvatarItemId\":\"\"}}]}",
        "FaceFeatures": "{\"ver\":-1,\"eyeId\":\"R30ouUXZOkijKBvQhA2G7A\",\"eyePos\":{\"x\":0.0,\"y\":-0.0987447202205658},\"eyeScl\":0.05000000074505806,\"mouthId\":\"pc1z8k98X0ae0Nab-IKhfA\",\"mouthPos\":{\"x\":0.0,\"y\":0.0},\"mouthScl\":0.0,\"hairPrimaryColorId\":\"\",\"hairSecondaryColorId\":\"Kav8RGYTCEy7zPPtL8uWaQ\",\"hairPatternId\":\"\",\"beardColorId\":\"Kav8RGYTCEy7zPPtL8uWaQ\",\"beardSecondaryColorId\":\"Kav8RGYTCEy7zPPtL8uWaQ\",\"beardPatternId\":\"\",\"faceShapeId\":\"yR4oYZr_AUSynXCgwS2lGw\",\"bodyShapeId\":\"RExJfB99XEqN4K2-x5QOBQ\",\"useHatAnchorParams\":true,\"useHelmetHair\":1,\"hideEars\":true,\"hatAnchorParams\":{\"NormalizedPosition\":{\"x\":0.5,\"y\":0.5590000152587891},\"HemisphereOffsets\":{\"x\":0.0,\"y\":-0.009867330081760884,\"z\":0.009999999776482582},\"HemisphereRotations\":{\"x\":0.0,\"y\":0.0,\"z\":0.0}},\"baseAvatarType\":\"\"}",
        "SkinColor": "Xac-W_R330KfOz-pQla9qg",
        "HairColor": "befcc00a-a2e6-48e4-864c-593d57bbbb5b",
        "CustomAvatarItems": []
    }
    with open(f"{data.saveDataPath}Profile\\userid.txt", "w") as f:
        f.write(str(playerId))
    with open(f"{data.saveDataPath}Profile\\username.txt", "w") as f:
        f.write(name)
    with open(f"{data.saveDataPath}Profile\\avatar.json", "w") as f:
        json.dump(avatar, f, indent=2)
    profileimage = requests.request("GET", profileimageUrl)
    if profileimage.status_code != 200:
        print(f"ERROR HTTP: {profileimage.status_code} on profileimage download")
        input()
        sys.exit()
    with open(f"{data.saveDataPath}Profile\\profileimage.jpg", "wb") as f:
        f.write(profileimage.content)