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
                current_account = row['current_account']
                savings_account = row['savings_account']
                credit_cards = row['credit_cards']
                isa = row['isa']
                mortgages = row['mortgages']
                branches = row['branches']
                atm_limit = row['atm_limit']
                online_services = row['online_services']
                mobile_services = row['mobile_services']
                joint_accounts = row['joint_accounts']
                child_accounts = row['child_accounts']
                overall_service = row['overall_service']
                online_service = row['online_service']
                overdraft_service = row['overdraft_service']
                branch_service = row['branch_service']
                esg_rating = row['esg_rating']

                conn.execute(sql.text(
                    'INSERT INTO Banks (bank_name, current_account, savings_account, credit_cards, isa, mortgages, branches, '
                    'atm_limit, online_services, mobile_services, joint_accounts, child_accounts, overall_service, '
                    'online_service, overdraft_service, branch_service, esg_rating) VALUES (:bank_name, '
                    ':current_account, :savings_account, :credit_cards, :isa, :mortgages, :branches, :atm_limit, '
                    ':online_services, :mobile_services, :joint_accounts, :child_accounts, :overall_service, '
                    ':online_service, :overdraft_service, :branch_service, :esg_rating)'),
                    {'bank_name': bank_name, 'current_account': current_account,
                     'savings_account': savings_account, 'credit_cards': credit_cards, 'isa': isa,
                     'mortgages': mortgages, 'branches': branches, 'atm_limit': atm_limit,
                     'online_services': online_services,
                     'mobile_services': mobile_services, 'joint_accounts': joint_accounts,
                     'child_accounts': child_accounts, 'overall_service': overall_service,
                     'online_service': online_service, 'overdraft_service': overdraft_service,
                     'branch_service': branch_service, 'esg_rating': esg_rating})

            # Commit the changes and close the connection
            conn.commit()
            conn.close()


def populate_application_features():
    with app.app_context():
        # Open the CSV file and read its contents
        with open('csv files/application_features.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Connect to the database and create a cursor
            conn = db.session.connection()

            # Iterate through each row in the CSV file and insert it into the database
            for row in reader:
                bank_id = row['bank_id']
                freeze_card = row['freeze_card']
                spending_notifications = row['spending_notifications']
                spending_categories = row['spending_categories']
                turn_off_certain_spending = row['turn_off_certain_spending']
                budgeting_goals = row['budgeting_goals']

                # Execute the SQL statement with the parameters for the current row
                conn.execute(sql.text(
                    'INSERT INTO application_features (bank_id, freeze_card, spending_notifications, spending_categories, '
                    'turn_off_certain_spending, budgeting_goals) '
                    'VALUES (:bank_id, :freeze_card, :spending_notifications, :spending_categories, :turn_off_certain_spending, '
                    ':budgeting_goals)'),
                    {'bank_id': bank_id, 'freeze_card': freeze_card, 'spending_notifications': spending_notifications,
                     'spending_categories': spending_categories, 'turn_off_certain_spending': turn_off_certain_spending,
                     'budgeting_goals': budgeting_goals})

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
