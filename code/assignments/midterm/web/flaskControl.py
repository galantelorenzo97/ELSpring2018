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
    peopleCount = result[2]
    return render_template('index.html', peopleCount = peopleCount)


# get the people data from database
@app.route("/catch")
def data():
    db = sqlite3.connect('../log/peopleLog.db')
    db.row_factory = sqlite3.Row

    cursor = db.cursor()
    cursor.execute("SELECT * FROM peopleLog")

    entry = cursor.fetchall()
    data = []
    for row in entry:
        data.append(list(row))

    return Response(json.dumps(data),  mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
