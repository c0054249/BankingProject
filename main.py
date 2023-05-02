from datetime import timedelta
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import current_user
from content.web_scraping import init_web_scraping

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banks.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


@app.route('/')
def index():  # put application's code here
    top_stories = init_web_scraping()
    return render_template('index.html', stories=top_stories, current_user=current_user)


# 404 error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_codes/404.html'), 404


# import blueprint
from search_algorithm.views import search_algorithm_blueprint
from content.blueprints import blueprint

# register blueprint with app
app.register_blueprint(search_algorithm_blueprint)

# register blueprint with app
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run()
