from tools.database import database


# @todo Connect freshly to the database and execute the operation
class schema(database):
    def __init__(self):
        super().__init__()

    def table_exists(self, table="") -> bool:
        exists = len(self.query(f"PRAGMA TABLE_INFO(`{table}`);")) >= 1
        return exists

    def create_table(self, table, columns=()):
        _COLUMNS = ",".join([f"`{column}` {datatype} NOT NULL" for column, datatype in columns])
        skeleton_sql = f"CREATE TABLE IF NOT EXISTS `{table}` ({_COLUMNS});"
        self.query(skeleton_sql)
        print("# @todo: Adjust the primary key in - ", table)

    def columns_match(self, table="", config={}) -> bool:
        return False

    def get_tables(self):
        # skip config tables
        # List all other tables
        tables_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'config_%';"
        tables = self.query(tables_sql)
        return tables

    def table_id(self, table_name=""):
        sql = "SELECT table_id FROM config_tables WHERE table_name=? LIMIT 1;"
        # @todo Data may not be available
        return self.query(sql, (table_name,))[0][0]

    def pragma_info(self, table):
        return self.query(f"PRAGMA TABLE_INFO(`{table}`);")

