from tools import meta
from tools.database import database


class exporter(database):
    def __init__(self):
        super().__init__()

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
