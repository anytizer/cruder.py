import sqlite3
import config


class database:
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect(config.database_file)
        self.connection.row_factory = sqlite3.Row

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def query(self, sql="", parameters=[]) -> []:
        cursor = self.connection.cursor()
        cursor.execute(sql, parameters)
        data = cursor.fetchall()
        return data

    def row(self, sql="", parameters=[]) -> []:
        cursor = self.connection.cursor()
        cursor.execute(sql, parameters)
        data = cursor.fetchone()
        return data
