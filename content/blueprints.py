
from flask import Blueprint, render_template, request, Flask

blueprint = Blueprint('blueprints', __name__, template_folder='templates')


@blueprint.route('/choosing_a_bank')
def choosing_a_bank():
    return render_template('choosing_a_bank.html')