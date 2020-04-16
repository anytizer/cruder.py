import sqlite3
from configs import config


class database:
    connection = None

    def __init__(self):
        try:
            self.connection = sqlite3.connect(config.DATABASE)
        except:
            raise Exception("Could not connect to database")

        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA encoding = 'UTF-8';")
        self.connection.execute("PRAGMA count_changes = ON;")
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.connection.execute("BEGIN TRANSACTION;")

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
