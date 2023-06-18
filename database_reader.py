import sqlite3
import pathlib
from pathlib import Path


class database_connector:
    def __init__(self):
        self.db_path = Path(pathlib.Path.cwd(), 'data_dump.db')
        '''connecting to the database'''
    def database_connect(self):      
        try:
            sqlite_connection = sqlite3.connect(self.db_path)
            return sqlite_connection
        except sqlite3.Error as error:
            print("SQLite connection error", error)

    def search(self) -> list:
        """searching for cities """
        db_connection = self.db.database_connect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT DISTINCT city FROM airports ORDER BY city ASC")
        return [city for cities in cursor.fetchall() for city in cities]