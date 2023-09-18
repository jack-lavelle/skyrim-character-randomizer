import mysql.connector
from utilities import read_json_as_dict


# Rewriting this file following https://stackoverflow.com/questions/14503973/python-global-keyword-vs-pylint-w0603
class Database:
    mysql_config = None
    cursor = None
    conn = None

    def __init__(self, mysql_config=None):
        if mysql_config:
            self.mysql_config = mysql_config
        else:
            self.mysql_config = read_json_as_dict("config.json")["mysql_config"]

    def open(self) -> bool:
        # Open the connection to the database to make a query.
        try:
            self.conn = mysql.connector.connect(**self.mysql_config)
        except mysql.connector.errors.ProgrammingError as exception:
            raise ValueError(
                f"Error occured while connecting to database. Something is probably wrong with the database config properties: {self.mysql_config}."
            ) from exception

        self.cursor = self.conn.cursor()

    def close(self) -> bool:
        self.cursor.close()
        self.conn.close()

    def write_suggestion(self, suggestion: str) -> str:
        self.open()
        insert_query = "INSERT INTO suggestions (suggestion) VALUES (%s)"
        self.cursor.execute(insert_query, (suggestion,))
        self.conn.commit()
        self.close()
        return "Thank you for your suggestion!"

    def create_suggestions_table(self):
        self.open()
        # Drop the table if it exists
        drop_table_query = "DROP TABLE IF EXISTS suggestions;"
        self.cursor.execute(drop_table_query)

        # Create the suggestions table
        create_table_query = """
            CREATE TABLE suggestions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            suggestion TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        self.cursor.execute(create_table_query)

        self.conn.commit()
        self.close()
        print("`suggestions` table was successfully created.")

    def check_database_exists(self, database_name) -> bool:
        self.open()
        self.cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = self.cursor.fetchone()

        self.close()

        if result:
            return True
        else:
            return False

    def check_table_exists(self, table_name) -> bool:
        self.open()
        # Check if the table exists
        self.cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = self.cursor.fetchone()

        self.close()
        if result:
            return True
        else:
            return False

    def retrieve_first_n_suggestions(self, n: int) -> list:
        self.open()
        query = f"""SELECT suggestion FROM `skyrim-character-generator`.suggestions LIMIT {n}"""
        self.cursor.execute(query)
        l = [row[0] for row in self.cursor]

        self.close()

        return l

    def retrieve_last_n_suggestions(self, n: int) -> list:
        self.open()
        query = f"""SELECT suggestion FROM `skyrim-character-generator`.suggestions ORDER BY id DESC LIMIT {n}"""
        self.cursor.execute(query)
        l = [row[0] for row in self.cursor]

        self.close()

        return l
