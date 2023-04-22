from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

PATH = "./score.db"

def fit():
    db = sqlite3.connect(PATH)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS form1(id TEXT, name TEXT, score FLOAT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS form2(id TEXT, name TEXT, detailed TEXT, score FLOAT, date TEXT)")
    cursor.close()

@app.route("/test")
def test():
    return render_template("test.html")

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

@app.route("/getrecord", methods=['GET'])
def getMemberRecord():
    print("a")
    db = sqlite3.connect(PATH)
    cursor = db.cursor()
    cursor.execute("SELECT name, detailed, score, date FROM form2")
    result = cursor.fetchall()
    data = []
    for i in result:
        data.append({"class": "209",
                     "date": i[3],
                     "name": i[0],
                     "points": i[2],
                     "reason": i[1]})
    return {"data":data}

if __name__ == "__main__":
    fit()
    app.run('0.0.0.0', debug = True)