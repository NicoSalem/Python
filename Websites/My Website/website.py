from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/experience", methods=["GET"])
def experience():
    return render_template("experience.html")

if __name__=="__main__":
    app.run()