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
import ProgramUtils

import data


name = f"{__name__}.py"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
CORS(app)

heartbeat = {
    "playerId": 1,
    "statusVisibility": 3,
    "platform": -1,
    "deviceClass": 0,
    "vrMovementMode": 0,
    "roomInstance": None,
    "lastOnline": None,
    "isOnline": False,
    "appVersion": "20221209"
}

playerId = player_API.getmyPlayer()["accountId"]

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/player/login", methods=["POST"])
def playerlogin():
    global heartbeat
    heartbeat.update({
        "lastOnline": ProgramUtils.getCurrentTime(),
        "roomInstance": None,
        "isOnline": True
    })
    return jsonify("")

@app.route("/player/logout", methods=["POST"])
def playerlogout():
    global heartbeat
    heartbeat.update({
        "lastOnline": ProgramUtils.getCurrentTime(),
        "roomInstance": None,
        "isOnline": False
    })
    return jsonify("")


@app.route("/player/heartbeat", methods=["POST"])
def playerheartbeat():
    return jsonify(heartbeat)

@app.route("/player/exclusivelogin", methods=["POST"])
def playerexclusivelogin():
    return jsonify("")

@app.route("/matchmake/none", methods=["POST"])
def matchmakenone():
    global heartbeat
    Authorization = request.headers.get("Authorization")
    heartbeat.update({
        "lastOnline": ProgramUtils.getCurrentTime(),
        "roomInstance": None,
        "isOnline": True
    })
    data = {
        "access_token": Authorization,
        "error_description":"",
        "error":"",
        "refresh_token": Authorization,
        "key":""
    }
    return jsonify(data)

@app.route("/matchmake/dorm", methods=["POST"])
def matchmakedorm():
    global heartbeat
    Authorization = request.headers.get("Authorization")
    room = room_API.findRoom("DormRoom")
    roomInstanceId = random.randint(1, 999999999)
    photonRoomId = "OldRecRoom2023-PROD-" + room["Name"] + str(room["SubRooms"][0]["SubRoomId"]) + str(room["RoomId"])
    roomInstance = {
        "roomInstanceId":roomInstanceId,
        "roomId":room["RoomId"],
        "subRoomId":room["SubRooms"][0]["SubRoomId"],
        "location":room["SubRooms"][0]["UnitySceneId"],
        "roomInstanceType":0,
        "photonRegionId":"EU",
        "photonRegion":"EU",
        "photonRoomId":photonRoomId,
        "name":name,
        "maxCapacity":4,
        "isFull":False,
        "isPrivate":False,
        "isInProgress":False,
        "matchmakingPolicy":0
    }
    heartbeat.update({
        "lastOnline": ProgramUtils.getCurrentTime(),
        "roomInstance": roomInstance,
        "isOnline": True
    })
    data1 = {
        "errorCode": 0,
        "roomInstance": roomInstance
    }
    print(data1)
    return jsonify(data1)

@app.route("/matchmake/room/<int:RoomId>", methods=["POST"])
def matchmakeId(RoomId):
    global heartbeat
    room = room_API.findRoomId(RoomId)
    roomInstanceId = random.randint(1, 999999999)
    photonRoomId = "OldRecRoom2023-PROD-" + room["Name"] + str(room["SubRooms"][0]["SubRoomId"]) + str(room["RoomId"])
    roomInstance = {
        "roomInstanceId":roomInstanceId,
        "roomId":room["RoomId"],
        "subRoomId":room["SubRooms"][0]["SubRoomId"],
        "location":room["SubRooms"][0]["UnitySceneId"],
        "roomInstanceType":0,
        "photonRegionId":"EU",
        "photonRegion":"EU",
        "photonRoomId":photonRoomId,
        "name":name,
        "maxCapacity":4,
        "isFull":False,
        "isPrivate":False,
        "isInProgress":False,
        "matchmakingPolicy":0
    }
    heartbeat.update({
        "lastOnline": ProgramUtils.getCurrentTime(),
        "roomInstance": roomInstance,
        "isOnline": True
    })
    data1 = {
        "errorCode": 0,
        "roomInstance": roomInstance
    }
    print(data1)
    return jsonify(data1)

def getheartbeat():
    return heartbeat

def run():
    Port = 5002
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port), ssl_context="adhoc")