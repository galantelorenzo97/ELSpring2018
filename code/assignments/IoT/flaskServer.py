#!/usr/bin/python


from flask import Flask, render_template, jsonify, Response
import sqlite3
import json

app = Flask(__name__)

# get most recent temp
@app.route("/")
def index():
    db = sqlite3.connect('./log/tempLog.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tempRecord")
    result = cursor.fetchone()
    print(result[1])
    temperature = result[1]
    return render_template('index.html', temperature = temperature)


# get the temp data from database
@app.route("/catch")
def data():
    db = sqlite3.connect('./log/tempLog.db')
    db.row_factory = sqlite3.Row

    cursor = db.cursor()
    cursor.execute("SELECT * FROM tempRecord")

    entry = cursor.fetchall()
    data = []
    for row in entry:
        data.append(list(row))

    return Response(json.dumps(data),  mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
