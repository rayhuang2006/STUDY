import sqlite3
import sys

PATH = "./score.db"
try:
    db = sqlite3.connect(PATH)
except Exception as e:
    print("[*] Exception!{}".format(e))
    sys.exit()

"""
form 1
id: TEXT
name: TEXT
score: FLOAT

form 2
id: TEXT
detailed: TEXT
score: FLOAT
date: TEXT
"""

def fit():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS form1(id TEXT, name TEXT, score FLOAT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS form2(id TEXT, detailed TEXT, score FLOAT, date TEXT)")
    cursor.close()

def appendNewUser(id, name):
    """
    Error code 0: existed user
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM form1 WHERE id=?", (id,))
    if cursor.fetchone():
        cursor.close()
        return 0

    cursor.execute("INSERT INTO form1 VALUES(?, ?, 0)", (id, name,))
    db.commit()
    print("Append new user successfully[id={}, name={}]".format(id, name))

def appendUserRecord(id, score, desc, date):
    """
    Error code 0: id not found
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM form1 WHERE id=?", (id,))
    if not cursor.fetchone():
        cursor.close()
        return 0
    
    cursor.execute("SELECT name, score FROM form1 WHERE id=?", (id,))
    tmp = cursor.fetchone()
    name, current = tmp[0], tmp[1]
    cursor.execute("UPDATE form1 SET score=? WHERE id=?", (current+score, id))
    cursor.execute("INSERT INTO form2 VALUES(?, ?, ?, ?)", (id, desc, score, date))
    db.commit()
    print("Append a new record[id={}, name={}, score={}->{}, detailed={}, date={}]".format(id, name, current, current+score, desc, date))

def queryUserScore(id):
    """
    Error code 0: id not found
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM form1 WHERE id=?", (id,))
    result = cursor.fetchone()
    if not result:
        cursor.close()
        return 0

    cursor.close()
    return result[1], result[2]

def main():
    fit()
    #cmd
    """
    Usage:
    exit
    fit
    anu -id -name
    aur -id -score -desc -date
    qus -id
    """
    flag = True 
    while(flag):
        cmd = str(input(">"))
        _cmd = cmd.split(" ")
        if _cmd[0] == "fit":
            fit()
            print("fit")
        elif _cmd[0] == "anu":
            if len(_cmd) != 3:
                print("Missing args({})".format(len(_cmd)))
                continue
            else:
                res = appendNewUser(_cmd[1], _cmd[2])
                if res == 0:
                    print("Existed user")
                    continue
        elif _cmd[0] == "aur":
            if len(_cmd) != 5:
                print("Missing args({})".format(len(_cmd)))
                continue
            else:
                try:
                    score = float(_cmd[2])
                except ValueError:
                    print("Unexpected type")
                    continue
                res = appendUserRecord(_cmd[1], score, _cmd[3], _cmd[4])
                if res == 0:
                    print("Id not found")
                    continue
        elif _cmd[0] == "qus":
            if len(_cmd) != 2:
                print("Missing args({})".format(len(_cmd)))
                continue
            else:
                res = queryUserScore(_cmd[1])
                if res == 0:
                    print("Id not found")
                    continue
                
                print("[{}]{} > {}".format(_cmd[1], res[0], res[1]))
        elif _cmd[0] == "exit":
            flag = False
        else:
            print("Unknown command \"{}\"".format(_cmd[0]))
            
if __name__ == "__main__":
    main()
