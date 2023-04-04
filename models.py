from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import db, app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banks.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class Banks(db.Model):
    __tablename__ = 'banks'

    id = db.Column("id", db.Integer, primary_key=True)
    bank_name = db.Column("bank_name", db.String, nullable=False)

    def __init__(self, bank_name):
        self.bank_name = bank_name


class Top_Rated(db.Model):
    __tablename__ = 'top_rated'

    top_rated_id = db.Column("top_rated_id", db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey(Banks.id), nullable=False)
    service = db.Column('service', db.String, nullable=False)
    overview = db.Column('overview', db.String, nullable=False)

    def __init__(self, bank_id, service, overview):
        self.bank_id = bank_id
        self.service = service
        self.overview = overview


class Services(db.Model):
    __tablename__ = 'services'

    services_id = db.Column("services_id", db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey(Banks.id), nullable=False)
    current_account = db.Column('current_account', db.String, nullable=False)
    savings_account = db.Column('savings_account', db.String, nullable=False)
    credit_cards = db.Column('credit_cards', db.String, nullable=False)
    isa = db.Column('isa', db.String, nullable=False)
    mortgages = db.Column('mortgages', db.String, nullable=False)

    def __init__(self, bank_id, current_account, savings_account, credit_cards, isa, mortgages):
        self.bank_id = bank_id
        self.current_account = current_account
        self.savings_account = savings_account
        self.credit_cards = credit_cards
        self.isa = isa
        self.mortgages = mortgages

class Bank_reputation(db.Model):
    __tablename__ = 'bank_reputation'

    reputation_id = db.Column("services_id", db.Integer, primary_key=True)



def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
