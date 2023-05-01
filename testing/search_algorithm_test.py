import unittest
from flask_testing import TestCase
from search_algorithm.views import app, db, calculate_match_percentage, return_database


class TestSearchAlgorithm(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banks.sqlite3'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # test for case when top rated service is queried
    def test_calculate_match_percentage_top_rated(self):
        # set variables for return database
        mobile_services = 'yes'
        service = 'Overdraft'
        count = 0
        banks_data = return_database(mobile_services, service, count)

        # Test variables for user preferences
        current_account = 'yes'
        savings_account = 'yes'
        credit_card = 'yes'
        isa = 'yes'
        mortgage = 'yes'
        branches = 250
        withdrawalLimit = 250
        online_services = 'yes'
        mobile_services = 'yes'
        joint_accounts = 'yes'
        child_accounts = 'yes'
        freeze_card = 'yes'
        instant_notifications = 'yes'
        spending_categories = 'yes'
        turn_off_spending = 'yes'
        spending_goals = 'yes'
        reputation = 'Overall'
        esg = 'yes'

        # Calculate match percentages for the banks top rate for overdraft services
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
            spending_goals,
            reputation,
            esg
        )

        # Expected match percentages for top rated banks for overdraft
        expected_percentages = [68.75, 68.75, 87.5]

        # Test if the calculated match percentages are equal to the expected percentages
        self.assertEqual(match_percentages, expected_percentages)

    # test for case when mobile services are required
    def test_calculate_match_percentage_with_mobile_services(self):
        # set variables for return database
        mobile_services = 'yes'
        service = 'Overdraft'
        count = 1
        banks_data = return_database(mobile_services, service, count)

        # Test variables for user preferences
        current_account = 'yes'
        savings_account = 'yes'
        credit_card = 'na'
        isa = 'na'
        mortgage = 'yes'
        branches = 250
        withdrawalLimit = 400
        online_services = 'yes'
        mobile_services = 'yes'
        joint_accounts = 'yes'
        child_accounts = 'yes'
        freeze_card = 'yes'
        instant_notifications = 'yes'
        spending_categories = 'no'
        turn_off_spending = 'yes'
        spending_goals = 'no'
        reputation = 'Branch'
        esg = 'yes'

        # Calculate match percentages for first three banks returned
        match_percentages = calculate_match_percentage(
            banks_data[:3],
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
            spending_goals,
            reputation,
            esg
        )

        # Expected match percentages for top rated banks for overdraft
        expected_percentages = [52.50, 58.75, 52.50]

        # Test if the calculated match percentages are equal to the expected percentages
        self.assertEqual(match_percentages, expected_percentages)

    # test for case when no mobile services are required
    def test_calculate_match_percentage_without_mobile_services(self):
        # set variables for return database
        mobile_services = 'no'
        service = 'Overdraft'
        count = 1
        banks_data = return_database(mobile_services, service, count)

        # Test variables for user preferences
        current_account = 'yes'
        savings_account = 'yes'
        credit_card = 'na'
        isa = 'na'
        mortgage = 'yes'
        branches = 250
        withdrawalLimit = 250
        online_services = 'yes'
        mobile_services = 'no'
        joint_accounts = 'yes'
        child_accounts = 'yes'
        freeze_card = 'yes'
        instant_notifications = 'yes'
        spending_categories = 'no'
        turn_off_spending = 'yes'
        spending_goals = 'no'
        reputation = 'Overall'
        esg = 'yes'

        # Calculate match percentages for first three banks returned
        match_percentages = calculate_match_percentage(
            banks_data[:3],
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
            spending_goals,
            reputation,
            esg
        )

        # round each percentage to 2 decimal places
        match_percentages = [round(x, 2) for x in match_percentages]

        # Expected match percentages for top rated banks for overdraft
        expected_percentages = [45.45, 54.55, 54.55]

        # Test if the calculated match percentages are equal to the expected percentages
        self.assertEqual(match_percentages, expected_percentages)

if __name__ == '__main__':
    unittest.main()
