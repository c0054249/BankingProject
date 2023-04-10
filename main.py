from datetime import timedelta
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banks.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', current_user=current_user)


# import blueprint
from search_algorithm.views import search_algorithm_blueprint
from content.blueprints import blueprint

# register blueprint with app
app.register_blueprint(search_algorithm_blueprint)

# register blueprint with app
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run()
