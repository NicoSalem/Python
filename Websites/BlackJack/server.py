from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
app = Flask(__name__)
#socketio = SocketIO(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")
    
@app.route("/BlackJack", methods=["GET"])
def Bj():
    return render_template("BlackJack.html")

if __name__=="__main__":
    #socketio.run(app)
    app.run()
