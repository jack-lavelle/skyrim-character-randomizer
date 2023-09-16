import mysql.connector


mysql_config = {
    "host": "applefrogs.mysql.pythonanywhere-services.com",
    "user": "applefrogs",
    "password": "Sopdoo123!",
    "database": "applefrogs$skyrim-character-generator",
}


def write_suggestion(suggestion: str) -> str:
    # Connect to MySQL and save the suggestion
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    insert_query = "INSERT INTO suggestions (suggestion) VALUES (%s)"
    cursor.execute(insert_query, (suggestion,))
    conn.commit()
    cursor.close()
    conn.close()
    return "Thank you for your suggestion!"


def create_suggestions_table():
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # Drop the table if it exists
    drop_table_query = "DROP TABLE IF EXISTS suggestions;"
    cursor.execute(drop_table_query)

    # Create the suggestions table
    create_table_query = """
        CREATE TABLE suggestions (
           id INT AUTO_INCREMENT PRIMARY KEY,
           suggestion TEXT NOT NULL,
           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    cursor.execute(create_table_query)

    conn.commit()
    cursor.close()
    conn.close()
    print("suggestions table successfully created.")


def check_database_exists(database_name):
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # Check if the database exists
    cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return True
    else:
        return False


def check_table_exists(table_name):
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # Check if the table exists
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return True
    else:
        return False


def retrieve_first_n_suggestions(n: int):
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    query = (
        f"""SELECT suggestion FROM `skyrim-character-generator`.suggestions LIMIT {n}"""
    )
    cursor.execute(query)
    l = [row[0] for row in cursor]

    cursor.close()
    conn.close()

    return l
