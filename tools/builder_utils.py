from tools.database import database


class builder_utils(database):
    def __init__(self):
        super().__init__()

    def table_exists(self, table="") -> bool:
        exists = len(self.connection.execute(f"PRAGMA TABLE_INFO(`{table}`);").fetchall()) >= 1
        return exists

    def create_table(self, table, columns=()):
        _COLUMNS = ",".join([f"`{column}` {datatype} NOT NULL" for column, datatype in columns])
        skeleton_sql = f"CREATE TABLE IF NOT EXISTS `{table}` ({_COLUMNS});"
        self.connection.execute(skeleton_sql)
        print("Adjust the Primary Key in - ", table)

    def columns_match(self, table="", config={}) -> bool:
        return False

    def get_tables(self):
        # skip config tables
        tables_sql = "select name from sqlite_master where type='table' AND name NOT LIKE 'config_%';"
        tables = self.connection.execute(tables_sql).fetchall()
        return tables

    def table_id(self, table_name=""):
        sql = "SELECT table_id FROM config_tables WHERE table_name=? LIMIT 1;"
        return self.connection.execute(sql, (table_name,)).fetchone()[0]

    def pragma_info(self, table):
        return self.connection.execute(f"PRAGMA TABLE_INFO(`{table}`);").fetchall()

