from flask import Blueprint, render_template

search_algorithm_blueprint = Blueprint('search_algorithm', __name__, template_folder='templates')


@search_algorithm_blueprint.route('/search_home')
def search_home():
    return render_template('search_home.html')


@search_algorithm_blueprint.route('/services')
def services():
    return
