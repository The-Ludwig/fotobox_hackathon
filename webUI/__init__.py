from flask import Flask
from flask import Flask, render_template, request, jsonify
from .model import Image
from flask_socketio import SocketIO
# from ../camera.py import Camera
from datetime import datetime
import eventlet

eventlet.monkey_patch()

#camera = Camera
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
    Prev = camera.trigger()
    return render_template("snap.html", pic=Prev)


@app.route("/snap", methods=["POST"])
def prev():
    prev = camera.trigger()
    socket.emit("update")
    return jsonify(pic=prev)


@app.route("/snap", methods=["GET"])
def activateCamera():
    img = camera.trigger()
    Image.create(datetime=datetime.now(), loc=img)
    return render_template("snap.html", pic=img)


@app.route("/galery")
def galery():
    return render_template("galery.html", pics=Image.select())
