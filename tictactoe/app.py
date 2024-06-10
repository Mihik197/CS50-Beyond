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
        session["history"] = []
        session["winner"] = None

    return render_template("game.html", game=session["board"], turn=session["turn"], winner=session["winner"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    if session["board"][row][col] == None:
        session["board"][row][col] = session["turn"]
        session["history"].append({(row, col): session["turn"]})
        winner = check_winner(session["board"])
        if winner:
            session["winner"] = winner

        if session["turn"] == "X":
            session["turn"] = "O"
        else:
            session["turn"] = "X"

    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    session.pop("board", None)
    session.pop("turn", None)
    session.pop("history", None)
    session.pop("winner", None)
    return redirect(url_for("index"))

@app.route("/undo")
def undo():
    if session["winner"]:
        session["winner"] = None

    if session["history"]:
        last_move = session["history"][-1]
        for key, value in last_move.items():
            x, y = key
            session["turn"] = value
            session["board"][x][y] = None
        session["history"].pop()

    return redirect(url_for("index"))

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            return board[0][2]