from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

PATH = "./score.db"

def fit():
    db = sqlite3.connect(PATH)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS form1(id TEXT, name TEXT, score FLOAT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS form2(id TEXT, detailed TEXT, score FLOAT, date TEXT)")
    cursor.close()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/rule")
def rule_page():
    return render_template("regulation.html")

@app.route("/getrank", methods=['GET'])
def getMemberRank():
    db = sqlite3.connect(PATH)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM form1")
    result = cursor.fetchall()
    return {"data":result}

if __name__ == "__main__":
    fit()
    app.run('0.0.0.0', debug = True)