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
webNotify = None

from RecNet import player_API

playerId = player_API.getmyPlayer()["accountId"]

name = f"{__name__}.py"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
sock = Sock(app)
CORS(app)

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/web", methods=["GET"])
def web():
    return render_template("socket.html")

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