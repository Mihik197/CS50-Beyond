from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/<string:name>")
def index(name):
    now = datetime.datetime.now()
    is_new_years = now.month == 1 and now.day == 1
    return render_template("index.html", name=name.capitalize(), is_new_years=is_new_years)





# @app.route("/<string:name1>/<string:name2>")
# @app.route("/<string:name1>")
# def hello(name1, name2="mihik"):
#     name1 = name1.capitalize()
#     name2 = name2.capitalize() 
#     return f"hello {name1} and {name2}"