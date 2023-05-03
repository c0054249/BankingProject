
from flask import Blueprint, render_template, request, Flask

blueprint = Blueprint('blueprints', __name__, template_folder='templates')


@blueprint.route('/choosing_a_bank')
def choosing_a_bank():
    return render_template('choosing_a_bank.html')


@blueprint.route('/terminology')
def terminology():
    return render_template('terminology.html')


@blueprint.route('/search_overview')
def search_overview():
    return render_template('search_overview.html')


@blueprint.route('/about')
def about():
    return render_template('about.html')