
from app.main import get_db_connection


def test_database_connection():
    connection = get_db_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT DB_NAME()")

        result = cursor.fetchone()[0]

        assert result == "MissionUltronDB"
        print(f"Connected successfully to: {result}")

    finally:
        connection.close()
