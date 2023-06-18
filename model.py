import re


class AirportSearcher:
    def __init__(self):
        self.lat_min = "0"
        self.lat_max = "0"
        self.lon_min = "0"
        self.lon_max = "0"
        self.src_city = "0"
        self.dst_city = "0"
        self.db = None

    def set_db(self, db):
        """
        Set the database connection
        """
        self.db = db

    def search_airports(self) -> list:
        """
        seaching airports by coordinates from database
        """
        coordinates = (self.lat_min, self.lat_max, self.lon_min, self.lon_max)
        match = [re.match("^-?\d+$", item) for item in coordinates]
        if None in match:
            self.lat_min, self.lat_max, self.lon_min, self.lon_max = ("0", "0", "0", "0")
        db_connection = self.db.database_connect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT country, city, airport, latitude, longitude FROM airports WHERE"
                       f" latitude BETWEEN {self.lat_min} and {self.lat_max} and"
                       f" longitude BETWEEN {self.lon_min} and {self.lon_max}")
        return cursor.fetchall()
