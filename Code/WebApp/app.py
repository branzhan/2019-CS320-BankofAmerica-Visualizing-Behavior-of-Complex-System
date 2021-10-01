import json
from flask import Flask, render_template
# from flask_mysqldb import MySQL
import pandas as pd

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'MyDB'

# mysql = MySQL(app)

app = Flask(__name__)

nodeDf = pd.read_csv("Nodes.csv")
relDf = pd.read_csv("Relationships.csv")

@app.route("/")
def index():
    json = nodeDf.to_json(orient='records')
    return render_template("index.html", json=json)

if __name__ == "__main__":
    app.run(debug=True)