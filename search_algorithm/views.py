from flask import Blueprint, render_template, request

search_algorithm_blueprint = Blueprint('search_algorithm', __name__, template_folder='templates')


@search_algorithm_blueprint.route('/search_home')
def search_home():
    return render_template('search_home.html')


@search_algorithm_blueprint.route('/services')
def services():
    return render_template('search_services.html')


@search_algorithm_blueprint.route('/submit', methods=['POST'])
def submit():
    current_account = request.form['current_account']
    savings_account = request.form['savings_account']
    credit_card = request.form['credit_card']
    isa = request.form['isa']
    mortgage = request.form['mortgage']

    # Do something with the user's answers here, like store them in a database or print them out
    print(f"User selected {current_account} for current account")
    print(f"User selected {savings_account} for savings account")
    print(f"User selected {credit_card} for credit card")
    print(f"User selected {isa} for ISA")
    print(f"User selected {mortgage} for mortgage")

    return "Answers submitted successfully!"
