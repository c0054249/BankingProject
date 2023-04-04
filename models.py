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

# create an intermediate table for many to many relationship between the banks and top_rated tables
banks_top_rated = db.Table('banks_top_rated', db.Column('bank_id', db.Integer, db.ForeignKey('banks.id')),
                           db.Column('top_rated_id', db.Integer, db.ForeignKey('top_rated.top_rated_id')))


class Banks(db.Model):
    __tablename__ = 'banks'

    id = db.Column("id", db.Integer, primary_key=True)
    bank_name = db.Column("bank_name", db.String, nullable=False)

    # many to many relationship with top_rated table
    top_rated_bank = db.relationship('Top_rated', secondary=banks_top_rated, backref='bank')

    # one to one relationship with services table
    services = db.relationship('Services', backref='banks', uselist=False)

    # one to one relationship with bank reputation table
    bank_reputation = db.relationship('Bank_Reputation', backref='banks', uselist=False)

    # one to one relationship with application features table
    application_features = db.relationship('Application_Features', backref='banks', uselist=False)

    # one to one relationship with accessibility table
    accessibility = db.relationship('Accessibility', backref='banks', uselist=False)

    def __init__(self, bank_name):
        self.bank_name = bank_name


class Top_Rated(db.Model):
    __tablename__ = 'top_rated'

    top_rated_id = db.Column("top_rated_id", db.Integer, primary_key=True)
    service = db.Column('service', db.String, nullable=False)
    overview = db.Column('overview', db.String, nullable=False)

    def __init__(self, service, overview):
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


class Bank_Reputation(db.Model):
    __tablename__ = 'bank_reputation'

    reputation_id = db.Column("rep_id", db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey(Banks.id), nullable=False)
    overall_service = db.Column('overall_service', db.Integer, nullable=True)
    online_service = db.Column('online_service', db.Integer, nullable=True)
    overdraft_service = db.Column('overdraft_service', db.Integer, nullable=True)
    branch_service = db.Column('branch_service', db.Integer, nullable=True)
    esg_rating = db.Column('esg_rating', db.Integer, nullable=True)

    def __init__(self, bank_id, overall_service, online_service, overdraft_service, branch_service, esg_rating):
        self.bank_id = bank_id
        self.overall_service = overall_service
        self.online_service = online_service
        self.overdraft_service = overdraft_service
        self.branch_service = branch_service
        self.esg_rating = esg_rating


class Application_Features(db.Model):
    __tablename__ = 'application_features'

    application_feature_id = db.Column("app_feat_id", db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey(Banks.id), nullable=False)
    freeze_card = db.Column('freeze_card', db.String, nullable=False)
    spending_notifications = db.Column('spending_notifications', db.String, nullable=False)
    spending_categories = db.Column('spending_categories', db.String, nullable=False)
    turn_off_certain_spending = db.Column('turn_off_certain_spending', db.String, nullable=False)
    budgeting_goals = db.Column('budgeting_goals', db.String, nullable=False)

    def __init__(self, bank_id, freeze_card, spending_notifications, spending_categories, turn_off_certain_spending,
                 budgeting_goals):
        self.bank_id = bank_id
        self.freeze_card = freeze_card
        self.spending_notifications = spending_notifications
        self.spending_categories = spending_categories
        self.turn_off_certain_spending = turn_off_certain_spending
        self.budgeting_goals = budgeting_goals


class Accessibility(db.Model):
    __tablename__ = 'accessibility'

    accessibility_id = db.Column("accessibility", db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey(Banks.id), nullable=False)
    branches = db.Column("branches", db.Integer, nullable=False)
    atm_limit = db.Column("atm_limit", db.Integer, nullable=False)
    online_services = db.Column("online_services", db.String, nullable=False)
    mobile_services = db.Column("mobile_services", db.String, nullable=False)
    minimum_age = db.Column("minimum_age", db.String, nullable=False)

    def __init__(self, bank_id, branches, atm_limit, online_services, mobile_services, minimum_age):
        self.bank_id = bank_id
        self.branches = branches
        self.atm_limit = atm_limit
        self.online_services = online_services
        self.mobile_services = mobile_services
        self.minimum_age = minimum_age


def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
