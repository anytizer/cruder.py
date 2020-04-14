import sqlite3
import config


class database:
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect(config.database)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA encoding = 'UTF-8';")
        self.connection.execute("PRAGMA count_changes = ON;")
        self.connection.execute("PRAGMA foreign_keys = ON;")

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


class exporter(database):
    def export(self, table=""):
        export_query = f"SELECT * FROM `{table}` LIMIT 5000;"
        csv = self.query(export_query, ())
        columns = meta.columns(table)

        _csv = ["\t".join([f"{column}" for column in columns])]
        for r in csv:
            try:
                values = "\t".join(f"{str(column)}" for column in dict(r).values())
                _csv.append(values)
            except ValueError:
                pass
        return "\r\n".join(_csv)

    def importCSV(self, table="", csv="") -> bool:
        # for lines, import csv
        # self.query()
        return True

    def report(self, view_table="reports"):
        # @todo safeguard the view table variable
        # @todo _v_ attached. Other characters to be replaced
        records = self.query(f"SELECT * FROM `_v_{view_table}`")
        return records
