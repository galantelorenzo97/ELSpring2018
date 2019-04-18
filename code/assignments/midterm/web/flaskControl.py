#!/usr/bin/python


from flask import Flask, render_template, jsonify, Response, request
import sqlite3
import json

app = Flask(__name__)

# get most recent count
@app.route("/")
def index():
    db = sqlite3.connect('../doorLog/doorLog.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM doorLog")
    result = cursor.fetchone()
    print(result[1])
    return render_template('index.html')

#serve search.html if requested
@app.route("/search")
def search():
    return render_template('search.html')


# get the most recent data
@app.route("/catch")
def data():
    db = sqlite3.connect('../doorLog/doorLog.db')
    db.row_factory = sqlite3.Row

    cursor = db.cursor()
    cursor.execute("SELECT * FROM doorLog ORDER BY Date DESC LIMIT 10")

    entry = cursor.fetchall()
    data = []
    for row in entry:
        data.append(list(row))

    return Response(json.dumps(data),  mimetype='application/json')

#get number of database entries
@app.route("/count")
def dbcount():
    db = sqlite3.connect('../doorLog/doorLog.db')
    cursor = db.cursor()
    cursor.execute("SELECT count(*) from doorLog")
    count = cursor.fetchall()
    return Response(json.dumps({"data" : count[0][0]}), mimetype='application/json')

#Get closest database entry
@app.route("/searchResults", methods = ['POST', 'GET'])
def searchRes():
    nixTime = request.args.get('nixTime')
    db = sqlite3.connect('../doorLog/doorLog.db')
    cursor = db.cursor()

    cursor.execute("SELECT * FROM doorLog ORDER BY Date DESC WHERE UnixTime < " + nixTime + " LIMIT 1")
    recEntry = cursor.fetchone()

    return jsonify(recEntry);

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
