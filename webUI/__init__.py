from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
import peewee
from .model import Image
from time import sleep
from ../camera.py import Camera
from datetime import datetime

camera = Camera
app = Flask(__name__)
socket = SocketIO(app)


@app.before_first_request
def init():
    Image.create_table(safe=True)


@app.route("/")
def index():
    pics = Image.select()
    if len(pics) > 10:
        return render_template("index.html", pics=Image.select()[-10:-1])
    else:
        return render_template("index.html", pics=Image.select())


@app.route("/snap")
def snap():
    return render_template("snap.html", pic="default.jpg")


@app.route("snap", methods=["POST"])
def activateCamera():
    Prev = camera.trigger()
    return render_template("snap.html", Pic=Prev)


@app.route("snap", methods=["GET"])
def activateCamera():
    Prev = camera.trigger()
    Image.create(datetime=datetime.now(), loc=Prev)
    return render_template("snap.html", Pic=Prev)


@app.route("galery")
def galery():
    return render_template("galery.html", pics=Image.select())
