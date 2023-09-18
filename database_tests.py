import unittest
from database import Database

# test read and write
# test connectivity


class TestDatabase(unittest.TestCase):
    database = Database()

    def test_connection(self):
        self.database.open()
        self.assertIsNotNone(self.database.conn)

    def test_faulty_connect(self):
        mysql_config = {
            "host": "localhost",
            "user": "root",
            "password": "Sopdoo123!",
            "database": "does not exist",
        }
        faulty_database = Database(mysql_config)
        self.assertRaises(ValueError, faulty_database.open)

    def test_read_write(self):
        test_suggestion = "Test suggestion."
        self.database.write_suggestion(test_suggestion)
        received_suggestion = self.database.retrieve_last_n_suggestions(1)[0]
        self.assertEqual(test_suggestion, received_suggestion)


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit as e:
        pass
