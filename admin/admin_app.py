import time
from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify, send_file
#import database
import hashlib
import sqlite3
import datetime
import hashlib
from datetime import datetime
import csv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

app = Flask(__name__)
app.secret_key = "teszt_kulcs"

db = create_engine('sqlite:///../data.db', echo=True)
meta = MetaData()

users = Table(
    "users",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('passw', String, nullable=False)
)
meta.create_all(db)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=4000)