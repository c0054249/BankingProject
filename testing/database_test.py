import unittest
from search_algorithm.views import return_database, app, db
from sqlalchemy import text


# testing for return_database function in search algorithm script to ensure correct database return functionality
class TestReturnDatabase(unittest.TestCase):

    # set app context and database for each test
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        self.connection = db.session.connection()

    # clean context and connection after each test
    def tearDown(self):
        self.connection.close()
        self.app_context.pop()

    # test case where mobile services are not required and count = 1
    def test_return_database_with_mobile_services_and_count_1(self):
        result = return_database('yes', 'Overdraft', 1)
        expected_query = text(
            "SELECT * FROM banks JOIN application_features ON banks.id = application_features.bank_id")
        expected_result = self.connection.execute(expected_query)
        expected_rows = expected_result.fetchall()
        expected_keys = expected_result.keys()
        expected_results = [dict(zip(expected_keys, row)) for row in expected_rows]
        self.assertEqual(result, expected_results)


if __name__ == '__main__':
    unittest.main()
