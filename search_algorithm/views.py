from flask import Blueprint, render_template, request

search_algorithm_blueprint = Blueprint('search_algorithm', __name__, template_folder='templates')


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

    # application features
    freeze_card = request.form['freezeCard']
    instant_notifications = request.form['instantNotifications']
    spending_categories = request.form['spendingCategories']
    turn_off_spending = request.form['turnOffSpending']
    spending_goals = request.form['spendingGoals']

    print(f"User selected {current_account} for current account")
    print(f"User selected {savings_account} for savings account")
    print(f"User selected {credit_card} for credit card")
    print(f"User selected {isa} for ISA")
    print(f"User selected {mortgage} for mortgage")
    print(f"User selected {branches} for number of branches")
    print(f"User selected {withdrawalLimit} for maximum withdrawal limit from atm's")
    print(f"User selected {online_services} for online services")
    print(f"User selected {mobile_services} for mobile services")
    print(f"User selected {freeze_card} for freeze card")
    print(f"User selected {instant_notifications} for instant notifications")
    print(f"User selected {spending_categories} for spending categories")
    print(f"User selected {turn_off_spending} for turn off certain spending")
    print(f"User selected {spending_goals} for spending goals")


    return "Answers submitted successfully!"
