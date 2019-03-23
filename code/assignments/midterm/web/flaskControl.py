#!/usr/bin/python


from flask import Flask, render_template, jsonify, Response
import sqlite3
import json

app = Flask(__name__)

# get most recent count
@app.route("/")
def index():
    db = sqlite3.connect('../logPeople/peopleLog.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM peopleLog")
    result = cursor.fetchone()
    print(result[2])
    temperature = result[2]
    return render_template('index.html')


# get the most recent data
@app.route("/catch")
def data():
    db = sqlite3.connect('../logPeople/peopleLog.db')
    db.row_factory = sqlite3.Row

    cursor = db.cursor()
    cursor.execute("SELECT * FROM peopleLog LIMIT 10")

    entry = cursor.fetchall()
    data = []
    for row in entry:
        data.append(list(row))

    return Response(json.dumps(data),  mimetype='application/json')

#get number of database entries
@app.route("/count")
def dbcount():
    con = sqlite3.connect('../logPeople/peopleLog.db')
    cur = con.cursor()
    cur.execute("SELECT count(*) from peopleLog")
    count = cur.fetchall()
    return Response(json.dumps({"data" : count[0][0]}), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
