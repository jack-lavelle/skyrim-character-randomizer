import mysql.connector

mysql_config = {
    "host": "applefrogs.mysql.pythonanywhere-services.com",
    "user": "applefrogs",
    "password": "Sopdoo123!",
    "database": "applefrogs$skyrim-character-generator",
}


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


check_database_exists("applefrogs$default")
