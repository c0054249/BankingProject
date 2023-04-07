import csv
import sqlite3
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import sql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banks.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


# function to populate the banks table in the database
def populate_banks():
    with app.app_context():
        # Open the CSV file and read its contents
        with open('csv files/banks.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Connect to the database and create a cursor
            conn = db.session.connection()

            # Iterate through each row in the CSV file and insert it into the database
            for row in reader:
                bank_name = row['bank_name']

                conn.execute(sql.text('INSERT INTO Banks (bank_name) VALUES (:bank_name)'), {'bank_name': bank_name})

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
