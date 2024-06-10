from flask import Flask, redirect, render_template, session, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]] 
        session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    if session["board"][row][col] == None:
        session["board"][row][col] = session["turn"]

        if session["turn"] == "X":
            session["turn"] = "O"
        else:
            session["turn"] = "X"

    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    session.pop("board", None)
    session.pop("turn", None)
    return redirect(url_for("index"))