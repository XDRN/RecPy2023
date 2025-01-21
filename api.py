from flask import Flask, request, jsonify, send_file, redirect, make_response, url_for, render_template, Response, abort, session
from flask_cors import CORS
import asyncio
import functools
import json
import requests
import random
import colorama
from colorama import Fore
import os
import base64
import sys
from enum import Enum
import jwt

from RecNet import player_API, room_API

import Matchmaking
import ProgramUtils

import data

savedata = data.saveDataPath

room_API.init()

room_API.loadRooms()
room_API.loadUnityAssets()

#print(room_API.unityAssets)

name = f"{__name__}.py"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
CORS(app)

playerId = player_API.getmyPlayer()["accountId"]

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/api/versioncheck/v4", methods=["GET"])
def apiversioncheckv4():
    return jsonify({"VersionStatus":0})

@app.route("/api/config/v1/amplitude", methods=["GET"])
def apiconfigv1amplitud():
    return jsonify({
        "AmplitudeKey":"e1693a1003671058b6abc356c8ba8d59",
        "UseRudderStack":True,
        "RudderStackKey":"23NiJHIgu3koaGNCZIiuYvIQNCu",
        "UseStatSig":True,
        "StatSigKey":"client-SBZkOrjD3r1Cat3f3W8K6sBd11WKlXZXIlCWj6l4Aje",
        "StatSigEnvironment":0
        }
    )

@app.route("/api/gameconfigs/v1/all", methods=["GET"])
def apigameconfigsv1all():
    with open(f"{data.saveDataPath}gameconfigs.json") as f:
        GC = json.load(f)
    return jsonify(GC)

@app.route("/api/auth/v1/eac/challenge", methods=["GET"])
def apiauthv1eacchallenge():
    data = "AQAAAHsg7mW5FQEE9HVl9EKMWXrqDzQxUCdgV/IPuQfbRgTx+cGnQqhhAgv1RvpihEC77gQ29JdoGFn2806Q+QPEj7nYg9C8pynbaiSVO8rKLJPvROsHuSXVJpQMv3TD8KyK3Y+n5bb86vAb5kRdZGD//uC8HY+D9jJLlEfTUlU="
    return jsonify(data)

@app.route("/api/auth/v1/cachedlogin/forplatformid/<int:platform>/<PlatformId>", methods=["GET"])
def apiauthv1cachedloginforplatformid0(platform, PlatformId):
    data = player_API.getcachedlogins(platform, PlatformId)
    return jsonify(data)

@app.route("/api/accounts/v1/account/bulk", methods=["GET"])
def apiaccountsv1accountbulk():
    data = [player_API.getmyPlayer()]
    return jsonify(data)

@app.route("/api/auth/v1/connect/token", methods=["POST"])
def apiauthv1connecttoken():
    roles = ["gameClient"]
    roles.append("moderator")
    roles.append("screenshare")
    roles.append("keepsake")
    roles.append("developer")
    token = jwt.encode({
        "iss": "https://zestrecauth.oldrecroom.com/",
        "client_id": "recnet",
        #"role": "gameclient",
        "role": roles,
        "sub": playerId,
        "auth_time": 1657773955,
        "idp": "local",
        "jti": "D9E0566B56518BCD20A64C2D6350C4E3",
        "sid": "564F9AAFC3AF41DD0A438CC19E899763",
        "iat": 1669575399,
        "scope": [],
        "amr": [
            "mfa"
        ]
    }, key="")
    data = {
        "access_token": token,
        "error_description":"",
        "error":"",
        "refresh_token": token,
        "key":""
    }
    return jsonify(data)

@app.route("/api/accounts/v1/account/me", methods=["GET"])
def apiaccountsv1accountme():
    data = player_API.getmyPlayer()
    return jsonify(data)

@app.route("/api/notify/v1/hub/v1/negotiate", methods=["POST"])
def apiotifyv1hubv1negotiate():
    Authorization = request.headers.get("Authorization")
    with open(f"{savedata}ip.txt") as f:
        ip2 = f.read()
    url2 = f"https://{ip2}:5001/"
    data = {
        "negotiateVersion":0,
        "SupportedTransports":[],
        "accessToken": Authorization,
        "url":url2
    }
    return jsonify(data)

@app.route("/api/econ/v1/api/objectives/v1/myprogress", methods=["GET"])
def apieconv1apiobjectivesv1myprogress():
    data = {
        "Objectives": [],
        "ObjectiveGroups": []
    }
    return jsonify(data)

@app.route("/api/customAvatarItems/v1/isCreationAllowedForAccount", methods=["GET"])
def apicustomAvatarItemsv1isCreationAllowedForAccount():
    return jsonify({"success":True,"value":None})

@app.route("/api/PlayerReporting/v1/moderationBlockDetails", methods=["GET"])
def apiPlayerReportingv1moderationBlockDetails():
    data = {"ReportCategory":0,"Duration":0,"GameSessionId":0,"Message":""}
    return jsonify(data)

@app.route("/api/relationships/v2/get", methods=["GET"])
def apirelationshipsv2get():
    data = []
    return jsonify(data)

@app.route("/api/player/settings/v1/playersettings", methods=["GET", "PUT"])
def apiplayersettingsv1playersettings():
    if request.method == "PUT":
        Json = request.form
        print(dict(Json))
        key = Json["key"]
        Value = Json["value"]
        with open(f"{data.saveDataPath}\\playersettings.json", "r") as f:
            PlayerSettings = json.load(f)
        for x in PlayerSettings:
            if x["Key"] == key:
                x["Value"] = Value
                with open(f"{data.saveDataPath}\\playersettings.json", "w") as f:
                    json.dump(PlayerSettings, f, indent=2)
                return jsonify(""), 200
        PlayerSettings.append({"Key":key,"Value":Value})
        with open(f"{data.saveDataPath}\\playersettings.json", "w") as f:
            json.dump(PlayerSettings, f, indent=2)
        return jsonify(""), 200
    elif request.method == "GET":
        with open(f"{data.saveDataPath}\\playersettings.json") as f:
            settings = json.load(f)
        return jsonify(settings)
    return abort(500)

@app.route("/api/econ/v1/api/avatar/v1/defaultunlocked", methods=["GET"])
def apieconv1apiavatarv1defaultunlocked():
    with open(f"{data.saveDataPath}AvatarItems.json") as f:
        aV = json.load(f)
    return jsonify(aV)

@app.route("/api/econ/v1/api/avatar/v4/items", methods=["GET"])
def apieconv1apiavatarv4items():
    with open(f"{data.saveDataPath}AvatarItems.json") as f:
        aV = json.load(f)
    return jsonify(aV)

@app.route("/api/econ/v1/api/avatar/v1/defaultbaseavataritems", methods=["GET"])
def apieconv1apiavatarv1defaultbaseavataritems():
    return jsonify([])

@app.route("/api/econ/v1/api/avatar/v2", methods=["GET"])
def apieconv1apiavatarv2():
    with open(f"{data.saveDataPath}Profile\\avatar.json") as f:
        aV = json.load(f)
    return jsonify(aV)

@app.route("/api/econ/v1/api/avatar/v2/set", methods=["POST"])
def apieconv1apiavatarv2set():
    print(request.get_json())
    with open(f"{data.saveDataPath}Profile\\avatar.json", "w") as f:
        json.dump(request.get_json(), f, indent=2)
    return jsonify("OK")

@app.route("/api/playerReputation/v2/bulk", methods=["GET"])
def apiplayerReputationv2bulk():
    data = {
        "AccountId": playerId,
        "IsCheerful": False,
        "Noteriety": 0.0,
        "SelectedCheer": 90,
        "CheerCredit": 99,
        "CheerGeneral": 0,
        "CheerHelpful": 0,
        "CheerCreative": 0,
        "CheerGreatHost": 0,
        "CheerSportsman": 0
    }
    return jsonify([data])

@app.route("/api/players/v2/progression/bulk", methods=["GET"])
def apiplayersv2progressionbulk():
    data = {
        "PlayerId": playerId,
        "Level": 1,
        "XP": 0
    }
    return jsonify([data])

@app.route("/api/chat/v1/thread", methods=["GET"])
def apichatv1thread():
    return jsonify([])

@app.route("/api/econ/v1/econ/customAvatarItems/v1/owned", methods=["GET"])
def apieconv1econcustomAvatarItemsv1owned():
    return jsonify({"Results": [], "TotalResults": 0})

@app.route("/api/quickPlay/v1/getandclear", methods=["GET"])
def apiquickPlayv1getandclear():
    return jsonify(None)

@app.route("/api/PlayerReporting/v1/hile", methods=["POST"])
def apiPlayerReportingv1hile():
    return jsonify(False)

@app.route("/api/config/v2", methods=["GET"])
def apiconfigv2():
    return jsonify(data.getConfig())

@app.route("/api/messages/v2/get", methods=["GET"])
def apimessagesv2get():
    return jsonify([])

@app.route("/api/config/v1/backtrace", methods=["GET"])
def apiconfigv1backtrace():
    return jsonify({
        "ReportBudget": 0,
        "FilterType": 0,
        "SampleRate": 0.025,
        "LogLineCount": 50,
        "CaptureNativeCrashes": 1,
        "ANRThresholdMs": 0,
        "MessageCount": 1000,
        "MessageRegex": "^Cannot set the parent of the GameObject .* while its new parent|^\\\u003E\\x2010x\\:\\x20|\\'LabelTheme\\' contains missing PaletteTheme reference on",
        "VersionRegex": ".*"
    })

@app.route("/api/rooms/v1/rooms", methods=["GET"])
def apiroomsv1rooms():
    name = request.args["name"]
    room = room_API.findRoom(name)
    if room is None:
        return abort(404)
    return jsonify(room)

@app.route("/api/rooms/v1/rooms/<int:RoomId>", methods=["GET"])
def apiroomsv1roomsId(RoomId):
    room = room_API.findRoomId(RoomId)
    if room is None:
        return abort(404)
    return jsonify(room)

@app.route("/api/rooms/v1/rooms/ownedby/me", methods=["GET"])
def apiroomsv1roomsownedbyme():
    return jsonify(room_API.rooms)

@app.route("/api/econ/v1/api/avatar/v3/saved", methods=["GET"])
def apieconv1apiavatarv3saved():
    return jsonify([])

@app.route("/api/econ/v1/api/equipment/v2/getUnlocked", methods=["GET"])
def apieconv1apiequipmentv2getUnlocked():
    with open(f"{data.saveDataPath}Equipments.json") as f:
        ejrgrg = json.load(f)
    return jsonify(ejrgrg)

@app.route("/api/econ/v1/api/consumables/v2/getUnlocked", methods=["GET"])
def apieconv1apiconsumablesv2getUnlocked():
    with open(f"{data.saveDataPath}Consumables.json") as f:
        ejrgrg = json.load(f)
    return jsonify(ejrgrg)

@app.route("/api/econ/v1/api/consumables/v1/consume", methods=["POST"])
def apieconv1apiconsumablesv1consume():
    return jsonify("")


@app.route("/api/econ/v1/api/avatar/v2/gifts", methods=["GET"])
def apieconv1apiavatav2gift():
    return jsonify([])

@app.route("/api/customAvatarItems/v1/isCreationEnabled", methods=["GET"])
def apicustomAvatarItemsv1isCreationEnabled():
    return jsonify(True)

@app.route("/api/customAvatarItems/v1/isRenderingEnabled", methods=["GET"])
def apicustomAvatarItemsv1isRenderingEnabled():
    return jsonify(True)

@app.route("/api/images/v2/named", methods=["GET"])
def apiimagesv2named():
    return jsonify([])

@app.route("/api/sanitize/v1/isPure", methods=["POST"])
def apisanitizev1ispure():
    return jsonify({"isPure":True})

@app.route("/api/playerevents/v1/all", methods=["GET"])
def apiplayereventsv1all():
    return jsonify({"Created": [], "Responses": []})

@app.route("/api/econ/v1/api/CampusCard/v1/UpdateAndGetSubscription", methods=["POST"])
def apieconv1apiCampusCardv1UpdateAndGetSubscription():
    return jsonify({
        "CanBuySubscription": True,
        "PlatformAccountSubscribedPlayerId": playerId,
        "Subscription": {
            "CreatedAt": "2024-10-07T22:48:32.3535893+01:00",
            "ExpirationDate": "9999-12-30T23:37:28.553+00:00",
            "IsActive": False,
            "IsAutoRenewing": False,
            "Level": 0,
            "ModifiedAt": "2024-10-07T22:48:32.3536127+01:00",
            "Period": 0,
            "PlatformId": "1",
            "PlatformPurchaseId": "0",
            "PlatformType": 0,
            "RecNetPlayerId": playerId,
            "SubscriptionId": 0
        }
    })

@app.route("/api/clubs/v1/announcements/v2/mine/unread", methods=["GET"])
def apiclubsv1announcementsv2mineunrea():
    return jsonify([])

@app.route("/api/clubs/v1/club/mine/member", methods=["GET"])
def apiclubsv1clubminemember():
    return jsonify([])

@app.route("/api/clubs/v1/announcements/v2/subscription/mine/unread", methods=["GET"])
def apiclubsv1announcementsv2subscriptionmineunread():
    return jsonify([])

@app.route("/api/PlayerReporting/v1/voteToKickReasons", methods=["GET"])
def apiPlayerReportingv1voteToKickReasons():
    return jsonify([])

@app.route("/api/announcement/v1/get", methods=["GET"])
def apiannouncementv1get():
    return jsonify([])

@app.route("/api/econ/v1/api/gamerewards/v1/pending", methods=["GET"])
def apieconv1apigamerewardsv1pending():
    return jsonify([])

@app.route("/api/rooms/v1/photon_access_token", methods=["GET"])
def apiroomsv1photon_access_token():
    dd = Matchmaking.getheartbeat()
    PhotonAccessToken = jwt.encode({"sub": str(playerId),"scope": "makerpen","aud": "gay"}, key="hey")
    Permissions = [
      {
        "Permission": "CAN_USE_MAKER_PEN",
        "Role": 0,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_USE_ROOM_RESET_BUTTON",
        "Role": 0,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_USE_DELETE_ALL_BUTTON",
        "Role": 0,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_SAVE_INVENTIONS",
        "Role": 0,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_SPAWN_INVENTIONS",
        "Role": 0,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_USE_PLAY_GIZMOS_TOGGLE",
        "Role": 0,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_USE_MAKER_PEN",
        "Role": 30,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_USE_ROOM_RESET_BUTTON",
        "Role": 30,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_USE_DELETE_ALL_BUTTON",
        "Role": 30,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_SAVE_INVENTIONS",
        "Role": 30,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_SPAWN_INVENTIONS",
        "Role": 30,
        "Override": True,
        "Type": 0,
        "Value": "True"
      },
      {
        "Permission": "CAN_USE_PLAY_GIZMOS_TOGGLE",
        "Role": 30,
        "Override": True,
        "Type": 0,
        "Value": "True"
      }
    ]
    data = {
        "RoomInstanceId": dd["roomInstance"]["roomInstanceId"],
        "PhotonAccessToken": PhotonAccessToken,
        "Permissions": Permissions
    }
    return jsonify(data)

@app.route("/api/rooms/v1/rooms/<int:RoomID>/interactionby/me", methods=["GET"])
def apiroomsv1roomsinteractionbyme(RoomID):
    return jsonify({"Cheered": False, "Favorited": False, "LastVisitedAt": None})

@app.route("/api/econ/v1/api/checklist/v1/current", methods=["GET"])
def apieconv1apichecklistv1current():
    return jsonify([])


@app.route("/api/inventions/v2/mine", methods=["GET"])
def apiinventionsv2mine():
    return jsonify([])

@app.route("/api/communityboard/v2/current", methods=["GET"])
def apicommunityboardv2current():
    print("Downloading communityboard config")
    fff = requests.request("GET", f"{data.dataUrl}communityboard.json")
    print("Done downloading communityboard config")
    if fff.status_code != 200:
        print(f"ERROR HTTP: {fff.status_code}")
        input()
        sys.exit()
    try:
        communityboard = fff.json()
    except:
        print(f"ERROR JSON: 0001")
        input()
        sys.exit()
    return jsonify(communityboard)

@app.route("/api/auth/v1/role/<role>/<int:playerId>", methods=["GET"])
def apiauthv1role(role, playerId):
    return jsonify(True)

@app.route("/api/rooms/v1/rooms/<int:RoomId>/subrooms/<SubRoomId>/permissions", methods=["PUT"])
def apiroomsvroomssubroomspermissions(RoomId, SubRoomId):
    return jsonify({"success":True,"error":""})

@app.route("/api/rooms/v1/unity_assets/<GUID>/<int:Target>/<int:Version>", methods=["GET"])
def apiroomsv1unityassetsGUIDTargetVersion(GUID, Target, Version):
    unitya = room_API.findUnityAsset(GUID)
    if unitya is None:
        return abort(404)
    return jsonify(unitya)

@app.route("/roomserver/unity_assets/<GUID>", methods=["GET"])
def apiroomsv1unityassetsGUID(GUID):
    return abort(404)#! not done
    unitya = room_API.findUnityAsset(GUID)
    if unitya is None:
        return abort(404)
    return jsonify(unitya)

@app.route("/api/images/v4/uploadsaved", methods=["POST"])
def apiimagesv4uploadsaved():
    name = f"{str(random.randint(100, 999999))}.png"
    request.files["image"].save(f"SaveData\\img\\{name}")
    return jsonify({"ImageName": name})


def run():
    Port = 5000
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port), ssl_context="adhoc")
