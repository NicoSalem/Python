from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
app = Flask(__name__)
socketio = SocketIO(app)

import requests
from bs4 import BeautifulSoup
import sqlite3
connection = sqlite3.connect('dataBase.db')
cursor = connection.cursor()


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/map", methods=["GET"])
def map():
    return render_template("map.html")

@app.route("/locations", methods=["GET"])
def locations():
    return render_template("locations.html")

def dataBaseFunction():
    cursor.execute() # write sql code using cursor methods
    connection.commit() #updates the db
    connection.close() #closes the db

@socketio.on("emit1")
def emit1Response(input1):
    from mp import main
    main(input1)
    print("map generated")
    # send("emit1")

@socketio.on("emit2")
def emit2Response(input1):
    from mp import coordinateString as cs
    print("cscscscscsscscc = " + cs)
    print(input1)
    emit('passing',cs)

if __name__=="__main__":
    socketio.run(app)
    #app.run()
