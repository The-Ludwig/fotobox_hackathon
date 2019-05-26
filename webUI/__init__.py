from flask import Flask
from flask import Flask, render_template, request, jsonify
from .model import Image
from . import camera
from . import photobox_bot
from datetime import datetime

app = Flask(__name__)

with open("telegramkey.txt", "r") as file:
    token = file.read()


def botTrigger():
    pic = camera.trigger()
    Image.create(datetime=datetime.now(), loc=pic)
    return pic

photobox_bot.startBot(botTrigger, token)
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


@app.route("/snap", methods=["GET"])
def snap():
    return render_template("snap.html")


@app.route("/snap", methods=["POST"])
def prev():
    pic = request.form.get('pic')
    Image.create(datetime=datetime.now(), loc=pic)


@app.route("/snap", methods=["PUT"])
def activateCamera():
    img = camera.trigger()
    return jsonify(pic=img)


@app.route("/galery", methods=["GET"])
def galery():
    return render_template("galery.html", pics=Image.select())


@app.route("/galery", methods=["PUT"])
def images():
    return jsonify(Image.select())
