from datetime import timedelta

from flask import Blueprint, render_template, request, Flask, current_app
import sqlite3

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

search_algorithm_blueprint = Blueprint('search_algorithm', __name__, template_folder='templates')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banks.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


@search_algorithm_blueprint.route('/search_home')
def search_home():
    return render_template('search_home.html')


@search_algorithm_blueprint.route('/services')
def services():
    return render_template('search.html')


@search_algorithm_blueprint.route('/submit', methods=['POST'])
def submit():
    # services responses
    current_account = request.form['current_account']
    savings_account = request.form['savings_account']
    credit_card = request.form['credit_card']
    isa = request.form['isa']
    mortgage = request.form['mortgage']

    # accessibility responses
    branches = int(request.form['branches'])
    withdrawalLimit = int(request.form['withdrawalLimit'])
    online_services = request.form['online_services']
    mobile_services = request.form['mobile_services']
    joint_accounts = request.form['joint_accounts']
    child_accounts = request.form['child_accounts']

    # application features
    freeze_card = request.form['freezeCard']
    instant_notifications = request.form['instantNotifications']
    spending_categories = request.form['spendingCategories']
    turn_off_spending = request.form['turnOffSpending']
    spending_goals = request.form['spendingGoals']

    # most important top rated feature
    service = request.form['service']

    # bank reputation
    reputation = request.form.get('reputation')

    print(f"User selected {current_account} for current account")
    print(f"User selected {savings_account} for savings account")
    print(f"User selected {credit_card} for credit card")
    print(f"User selected {isa} for ISA")
    print(f"User selected {mortgage} for mortgage")
    print(f"User selected {branches} for number of branches")
    print(f"User selected {withdrawalLimit} for maximum withdrawal limit from atm's")
    print(f"User selected {online_services} for online services")
    print(f"User selected {mobile_services} for mobile services")
    print(f"User selected {joint_accounts} for joint accounts")
    print(f"User selected {child_accounts} for child accounts")
    print(f"User selected {freeze_card} for freeze card")
    print(f"User selected {instant_notifications} for instant notifications")
    print(f"User selected {spending_categories} for spending categories")
    print(f"User selected {turn_off_spending} for turn off certain spending")
    print(f"User selected {spending_goals} for spending goals")
    print(f"User selected {service} for top rated service")
    print(f"User selected {reputation} for top rated service")

    return_database()

    return "Answers submitted successfully!"


def return_database():
    with app.app_context():
        # Get the database connection from the current app context
        conn = db.session.connection()

        # Create a text query using SQLAlchemy's text() function
        query = text("SELECT * FROM banks")

        # Execute the query and fetch all results as a list of dictionaries
        results = conn.execute(query).fetchall()

        # Close the connection
        conn.close()

        # Return the query results
        return results
