temp = {'AvatarItemDesc': '97253092-90ba-4ff2-b137-6324ab244d11,f335220c-f717-4d00-bed2-0e190ff65972', 'AvatarItemType': 0, 'PlatformMask': -1, 'FriendlyName': 'Dragon Lunar New Year Sweater', 'Tooltip': '', 'Rarity': -1, 'TagList': None, 'AvatarItemId': 6460, 'IsBaseAvatarItem': False, 'CreatedAt': '2024-02-08T23:18:49.287Z', 'ThumbnailImage': 'cdnz7aqx6sfcbsgge2d2pr2ai.jpg'}
import json
import ProgramUtils
import data
import sys
import requests


name = f"{__name__}.py"

def gen(readFile: str, writeFile: str):
    print(f"[{name}] Generating")
    sk = requests.request("GET", f"{data.dataUrl}AvatarItemWardrobeRuntimeConfig.json")
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
    teamAvatarItemSelections = sk["teamAvatarItemSelections"]
    teamEmissiveAvatarItemSelections = sk["teamEmissiveAvatarItemSelections"]
    defaultUnknownAvatarItemSelections = sk["defaultUnknownAvatarItemSelections"]
    defaultHelmetHairItemSelection1 = sk["defaultHelmetHairItemSelection"]
    helmetHairItemSelections = sk["helmetHairItemSelections"]
    defaultUnlockedAvatarItems = sk["defaultUnlockedAvatarItems"]
    initialAvatarItems = sk["initialAvatarItems"]
    defaultTorsoAvatarItems = sk["defaultTorsoAvatarItems"]
    defaultLegsAvatarItems = sk["defaultLegsAvatarItems"]
    defaultShoesAvatarItems = sk["defaultShoesAvatarItems"]
    allPossibleCombinations = sk["allPossibleCombinations"]

    num = 1
    avlist = []
    AvatarItemDescs = []

    for teamAvatarItemSelection in teamAvatarItemSelections:
        _avatarItemData = teamAvatarItemSelection["_avatarItem"]["_avatarItemData"]
        _avatarItemVisualData = teamAvatarItemSelection["_avatarItem"]["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    for teamEmissiveAvatarItemSelection in teamEmissiveAvatarItemSelections:
        _avatarItemData = teamEmissiveAvatarItemSelection["_avatarItem"]["_avatarItemData"]
        _avatarItemVisualData = teamEmissiveAvatarItemSelection["_avatarItem"]["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    for defaultUnknownAvatarItemSelection in defaultUnknownAvatarItemSelections:
        _avatarItemData = defaultUnknownAvatarItemSelection["_avatarItem"]["_avatarItemData"]
        _avatarItemVisualData = defaultUnknownAvatarItemSelection["_avatarItem"]["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    defaultHelmetHairItemSelection_avatarItemData = defaultHelmetHairItemSelection1["_avatarItem"]["_avatarItemData"]
    defaultHelmetHairItemSelection_avatarItemVisualData = defaultHelmetHairItemSelection1["_avatarItem"]["_avatarItemVisualData"]
    tghryyuer = False
    if defaultHelmetHairItemSelection_avatarItemVisualData.get("combinationGuid") is not None:
        if defaultHelmetHairItemSelection_avatarItemVisualData.get("combinationGuid") != "":
            tghryyuer = True
    if tghryyuer:
        AvatarItemDesc = f"{defaultHelmetHairItemSelection_avatarItemVisualData["prefabGuid"]},{defaultHelmetHairItemSelection_avatarItemVisualData["combinationGuid"]}"
    else:
        AvatarItemDesc = f"{defaultHelmetHairItemSelection_avatarItemVisualData["prefabGuid"]},"
    if not AvatarItemDesc in AvatarItemDescs:
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(defaultHelmetHairItemSelection_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    for helmetHairItemSelection in helmetHairItemSelections:
        _avatarItemData = helmetHairItemSelection["_avatarItem"]["_avatarItemData"]
        _avatarItemVisualData = helmetHairItemSelection["_avatarItem"]["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    for defaultUnlockedAvatarItem in defaultUnlockedAvatarItems:
        _avatarItemData = defaultUnlockedAvatarItem["_avatarItemData"]
        _avatarItemVisualData = defaultUnlockedAvatarItem["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)


    for initialAvatarItem in initialAvatarItems:
        _avatarItemData = initialAvatarItem["_avatarItemData"]
        _avatarItemVisualData = initialAvatarItem["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    for defaultTorsoAvatarItem in defaultTorsoAvatarItems:
        _avatarItemData = defaultTorsoAvatarItem["_avatarItemData"]
        _avatarItemVisualData = defaultTorsoAvatarItem["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    for defaultLegsAvatarItem in defaultLegsAvatarItems:
        _avatarItemData = defaultLegsAvatarItem["_avatarItemData"]
        _avatarItemVisualData = defaultLegsAvatarItem["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    for defaultShoesAvatarItem in defaultShoesAvatarItems:
        _avatarItemData = defaultShoesAvatarItem["_avatarItemData"]
        _avatarItemVisualData = defaultShoesAvatarItem["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    for allPossibleCombination in allPossibleCombinations:
        _avatarItemData = allPossibleCombination["_avatarItemData"]
        _avatarItemVisualData = allPossibleCombination["_avatarItemVisualData"]
        tghryyuer = False
        if _avatarItemVisualData.get("combinationGuid") is not None:
            if _avatarItemVisualData.get("combinationGuid") != "":
                tghryyuer = True
        if tghryyuer:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},{_avatarItemVisualData["combinationGuid"]}"
        else:
            AvatarItemDesc = f"{_avatarItemVisualData["prefabGuid"]},"
        if AvatarItemDesc in AvatarItemDescs:
            continue
        AvatarItemDescs.append(AvatarItemDesc)
        FriendlyNameSkinAssetName = str(_avatarItemData["Name"])
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace("(", "")
        FriendlyNameSkinAssetName = FriendlyNameSkinAssetName.replace(")", "")
        FriendlyName = f"{FriendlyNameSkinAssetName} ({AvatarItemDesc})"
        newAV = {
            'AvatarItemDesc': AvatarItemDesc, 
            'AvatarItemType': 0, 
            'PlatformMask': -1, 
            'FriendlyName': FriendlyName, 
            'Tooltip': '', 
            'Rarity': -1, 
            'TagList': None, 
            'AvatarItemId': num, 
            'IsBaseAvatarItem': False, 
            'CreatedAt': ProgramUtils.getCurrentTime(), 
            'ThumbnailImage': '3vltmrmtk3vjyyqkqeln9hdnb.jpg'
        }
        num += 1
        avlist.append(newAV)

    with open(writeFile, "w") as f:
        json.dump(avlist, f, indent=2)

    print(f"[{name}] Done")