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

playerId = player_API.getmyPlayer()["accountId"]

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/img/<path:imgName>", methods=["GET"])
def img(imgName):
    if imgName == "profileimage.jpg":
        with open(f"{data.saveDataPath}Profile\\profileimage.jpg", "rb") as f:
            img__ = f.read()
        hasj = "+VgcPPSK6ar2TFbvxFcekDTVFDAY42y4w4Z2erZpx52yfnq4C7xM5/kFLZ34i0s2G4dVqlI47+5lX5g1L8Ml0yn/XqALuK5J/WBf3nHB7Yu0oU3DPs7C2uvn8SPp8/fIu3LuofoUhQrCiZx6OofyuHzwqLw/2ZSyerVstUk6r+F9g4J4mmTWUHo48lc83rLtwPLEjoObPlriYqCRLWVcGiQUgvKAJM1JRi8aiL1tCeEstRdiX7XjfLUH8jF1GJe5t9oK52lrvZ6bRe1fQ=="
        data1 = {'Content-Signature': f'key-id=KEY:RSA:p1.rec.net; data={hasj}'}
        return Response(img__, 200, content_type="image/png", headers=data1)
    else:
        imgg = requests.request("GET", f"https://img.rec.net/{imgName}?sig=p1")
        hasj = "+VgcPPSK6ar2TFbvxFcekDTVFDAY42y4w4Z2erZpx52yfnq4C7xM5/kFLZ34i0s2G4dVqlI47+5lX5g1L8Ml0yn/XqALuK5J/WBf3nHB7Yu0oU3DPs7C2uvn8SPp8/fIu3LuofoUhQrCiZx6OofyuHzwqLw/2ZSyerVstUk6r+F9g4J4mmTWUHo48lc83rLtwPLEjoObPlriYqCRLWVcGiQUgvKAJM1JRi8aiL1tCeEstRdiX7XjfLUH8jF1GJe5t9oK52lrvZ6bRe1fQ=="
        data1 = {'Content-Signature': f'key-id=KEY:RSA:p1.rec.net; data={hasj}'}
        if imgg.status_code != 200:
            with open(f"{data.saveDataPath}Profile\\profileimage.jpg", "rb") as f:
                img__ = f.read()
            hasj = "+VgcPPSK6ar2TFbvxFcekDTVFDAY42y4w4Z2erZpx52yfnq4C7xM5/kFLZ34i0s2G4dVqlI47+5lX5g1L8Ml0yn/XqALuK5J/WBf3nHB7Yu0oU3DPs7C2uvn8SPp8/fIu3LuofoUhQrCiZx6OofyuHzwqLw/2ZSyerVstUk6r+F9g4J4mmTWUHo48lc83rLtwPLEjoObPlriYqCRLWVcGiQUgvKAJM1JRi8aiL1tCeEstRdiX7XjfLUH8jF1GJe5t9oK52lrvZ6bRe1fQ=="
            data1 = {'Content-Signature': f'key-id=KEY:RSA:p1.rec.net; data={hasj}'}
            return Response(img__, 200, content_type="image/png", headers=data1)
        return Response(imgg.content, 200, content_type="image/png", headers=data1)
    
@app.route("/config/LoadingScreenTipData", methods=["GET"])
def cdnconfigLoadingScreenTipData():
    print("Downloading LoadingScreenTipData")
    fff = requests.request("GET", f"{data.dataUrl}LoadingScreenTipData.json")
    print("Done downloading LoadingScreenTipData config")
    if fff.status_code != 200:
        print(f"ERROR HTTP: {fff.status_code}")
        input()
        sys.exit()
    try:
        LoadingScreenTipData = fff.json()
    except:
        print(f"ERROR JSON: 0001")
        input()
        sys.exit()
    return jsonify(LoadingScreenTipData)

def run():
    Port = 5003
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port), ssl_context="adhoc")