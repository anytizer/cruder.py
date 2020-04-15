import sqlite3
import uuid

from tools._capitalizer import capitalize


class builder_utils:
    connection = None

    def __init__(self):
        database = "database/garden.db"
        self.connection = sqlite3.connect(database)
        self.connection.execute("PRAGMA foreign_keys=ON;")
        self.connection.execute("BEGIN TRANSACTION;")

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def guid(self) -> str:
        return str(uuid.uuid4()).upper()

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

    def register_table(self, table="") -> str:
        table_prefix = ""
        pk_column = ""
        hidden_columns = ""
        extra_columns = ""
        do_crud = 1
        parent_column = ""

        insert_table = "INSERT OR IGNORE INTO config_tables (table_id, table_name, table_prefix, pk_column, hidden_columns, extra_columns, do_crud, parent_column) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
        data = (self.guid(), table, table_prefix, pk_column, hidden_columns, extra_columns, do_crud, parent_column)
        self.connection.execute(insert_table, data)

        table_id = self.connection.execute(f"SELECT table_id FROM config_tables WHERE table_name='{table}';").fetchall()[0][0]
        return table_id

    def register_showfields(self, table_id="", pragma=()):
        display_order = 0
        for column in pragma:
            cid, name, type, notnull, dflt_value, pk = column

            id = self.guid()
            column_name = name
            column_datatype = type
            showon_list = 0
            showon_edit = 0
            showon_detail = 0
            showon_insert = 0
            reserved_field = 0
            insert_showfields = """
            INSERT OR IGNORE INTO config_showfields (
                config_id, table_id, column_name, display_name, display_order, column_datatype,
                showon_list, showon_edit, showon_detail, showon_insert, reserved_field
            ) values(
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            );"""
            display_name = capitalize(column_name)
            display_order = display_order + 10
            data = (
                id, table_id, column_name, display_name, display_order, column_datatype, showon_list, showon_edit, showon_detail, showon_insert,
                reserved_field)
            self.connection.execute(insert_showfields, data)

    def register_colors(self, table_id="", pragma=()):
        for column in pragma:
            cid, name, type, notnull, dflt_value, pk = column

            id = self.guid()
            column_name = name
            color_back = "#000000"
            color_front = "#FFFFFF"
            color_hover = "#F0F0F0"

            insert_colors = """
            INSERT OR IGNORE INTO config_colors (
                config_id, table_id, column_name,
                color_back, color_front, color_hover
            ) VALUES (
                ?, ?, ?, ?, ?, ?
            );"""
            data = (id, table_id, column_name, color_back, color_front, color_hover)
            self.connection.execute(insert_colors, data)