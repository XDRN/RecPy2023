from flask import Flask, request, jsonify, send_file, redirect, make_response, url_for, render_template, Response, abort, session
from flask_sock import Sock
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
import enums
webNotify = None

from RecNet import player_API

playerId = player_API.getmyPlayer()["accountId"]

name = f"{__name__}.py"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
sock = Sock(app)
CORS(app)


def sendWS(type: enums.OICNNAPKPEL, msg: dict):
    sendData1 = {"id": type.name, "msg": msg}
    sendDatajson = {"type": 1, "target": "Notification", "arguments": [json.dumps(sendData1)]}
    sendData = json.dumps(sendDatajson)
    sendDataSTR = sendData + "\u001e"
    print(f"[{name}] sent data: " + str(sendDataSTR))
    webNotify.send(sendDataSTR)

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/web", methods=["GET"])
def web():
    d = {i.name: i.value for i in enums.OICNNAPKPEL}
    websockettypes = []
    for x, i in d.items():
        websockettypes.append({
            "id": i,
            "friendlyName": x
        })
    return render_template("socket.html", websockettypes=websockettypes)

@app.route("/api/socket/send", methods=["POST"])
def socketSend():
    if webNotify is None:
        return "<h1>You are not connected to RecRoom</h1>"
    print(request.form)
    type1 = request.form.get("type")
    msg = request.form.get("msg")
    type1 = enums.OICNNAPKPEL(int(type1))
    sendWS(type1, json.loads(msg))
    return "Done"

@app.route("/negotiate", methods=["POST"])
def negotiate():
    data = {
        "negotiateVersion": 0,
        "connectionId": playerId,
        "availableTransports": [
            {
                "transport": "WebSockets",
                "transferFormats": [
                    "Text",
                    "Binary"
                ]
            }
        ]
    }
    return jsonify(data)

@sock.route("/")
def notify(ws):
    global webNotify
    while True:
        webNotify = ws
        data = ws.receive()
        print(f"[{name}] received data: " + str(data))
        sentdata = data
        print(f"[{name}] sent data: " + str(sentdata))
        ws.send(sentdata)

def run():
    Port = 5001
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port), ssl_context='adhoc')