
#! this a old file
#! so yay am gay af
exit()

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


def run():
    Port = 5003
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port), ssl_context="adhoc")