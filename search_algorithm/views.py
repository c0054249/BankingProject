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

    return results(current_account, savings_account, credit_card, isa, mortgage, branches,
                   withdrawalLimit, online_services, mobile_services, joint_accounts, child_accounts, freeze_card,
                   instant_notifications, spending_categories, turn_off_spending, spending_goals)


def return_database(mobile_services):
    with app.app_context():
        # Get the database connection from the current app context
        conn = db.session.connection()

        # if the user requires mobile services then return the a joining application features related to the bank
        # else the user does not need to query this data
        # doing this stops returning unnecessary data
        if mobile_services == 'yes':
            query = text("SELECT * FROM banks JOIN application_features ON banks.id = application_features.bank_id")
        else:
            query = text("SELECT * FROM banks")

        result = conn.execute(query)
        rows = result.fetchall()
        keys = result.keys()  # Get the keys from the result object
        results = [dict(zip(keys, row)) for row in rows]

        # Close the connection
        conn.close()

        # Return the query results
        return results


def calculate_match_percentage(banks_data, current_account, savings_account, credit_card, isa, mortgage, branches,
                               withdrawalLimit, online_services, mobile_services, joint_accounts, child_accounts,
                               freeze_card, instant_notifications, spending_categories, turn_off_spending,
                               spending_goals):
    match_percentages = []

    # Loop through each bank in the results
    for bank_tuple in banks_data:

        # Initialize the match score and total score
        match_score = 0
        total_score = 0

        # Check each user preference and compare it with the bank's offering, incrementing the match_score and
        # total_score accordingly

        # Check current_account
        if current_account == bank_tuple['current_account']:
            match_score += 1
        total_score += 1

        # Check savings_account
        if savings_account == bank_tuple['savings_account']:
            match_score += 1
        total_score += 1

        # Check credit_card
        if credit_card == bank_tuple['credit_cards']:
            match_score += 1
        total_score += 1

        # Check ISA
        if isa == bank_tuple['isa']:
            match_score += 1
        total_score += 1

        # Check mortgage
        if mortgage == bank_tuple['mortgages']:
            match_score += 1
        total_score += 1

        # Check branches
        if branches >= bank_tuple['branches']:
            match_score += 1
        total_score += 1

        # Check withdrawalLimit
        if withdrawalLimit >= bank_tuple['atm_limit']:
            match_score += 1
        total_score += 1

        # Check online_services
        if online_services == bank_tuple['online_services']:
            match_score += 1
        total_score += 1

        # Check mobile_services
        if mobile_services == bank_tuple['mobile_services']:
            match_score += 1

            # Check freeze_card
            if freeze_card == bank_tuple['freeze_card']:
                match_score += 1
            total_score += 1

            # Check instant_notifications
            if instant_notifications == bank_tuple['spending_notifications']:
                match_score += 1
            total_score += 1

            # Check spending_categories
            if spending_categories == bank_tuple['spending_categories']:
                match_score += 1
            total_score += 1

            # Check turn_off_spending
            if turn_off_spending == bank_tuple['turn_off_certain_spending']:
                match_score += 1
            total_score += 1

            # Check spending_goals
            if spending_goals == 'yes' and bank_tuple['budgeting_goals']:
                match_score += 1
            total_score += 1
        total_score += 1

        # Check joint_accounts
        if joint_accounts == bank_tuple['joint_accounts']:
            match_score += 1
        total_score += 1

        # Check child_accounts
        if child_accounts == bank_tuple['child_accounts']:
            match_score += 1
        total_score += 1

        # Calculate the match percentage
        match_percentage = (match_score / total_score) * 100

        # Append the match percentage to the list
        match_percentages.append(match_percentage)

    return match_percentages


@search_algorithm_blueprint.route('/results')
def results(current_account, savings_account, credit_card, isa, mortgage, branches,
            withdrawalLimit, online_services, mobile_services, joint_accounts, child_accounts, freeze_card,
            instant_notifications, spending_categories, turn_off_spending, spending_goals):
    banks_data = return_database(mobile_services)
    match_percentages = calculate_match_percentage(
        banks_data,
        current_account,
        savings_account,
        credit_card,
        isa,
        mortgage,
        branches,
        withdrawalLimit,
        online_services,
        mobile_services,
        joint_accounts,
        child_accounts,
        freeze_card,
        instant_notifications,
        spending_categories,
        turn_off_spending,
        spending_goals
    )
    banks_and_scores = list(zip(banks_data, match_percentages))

    # Sort the banks and their scores based on the match percentage
    sorted_banks_and_scores = sorted(banks_and_scores, key=lambda x: x[1], reverse=True)

    return render_template('results.html', sorted_banks_and_scores=sorted_banks_and_scores)
