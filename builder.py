configs = {
    "employees": (
        ("employee_id", "text"),
        ("employee_name", "text"),
        ("employee_firstname", "text"),
        ("employee_lastname", "text"),
        ("employee_address", "text"),
        ("employee_phone", "text"),
    )
}

"""
DROP TABLE IF EXISTS config_showfields;
CREATE TABLE "config_showfields" (
	"config_id"	TEXT NOT NULL,
	"table_name"	TEXT NOT NULL,
	"column_name"	TEXT NOT NULL,
	"column_datatype"	TEXT NOT NULL,
	"showon_list"	TEXT NOT NULL,
	"showon_edit"	TEXT NOT NULL,
	"showon_detail"	TEXT NOT NULL,
	"showon_insert"	TEXT NOT NULL,
	"reserved_field"	TEXT NOT NULL,
	UNIQUE("table_name", "column_name"),
	PRIMARY KEY("config_id")
);
DROP TABLE IF EXISTS config_colors;
CREATE TABLE "config_colors" (
	"config_id"	TEXT NOT NULL,
	"table_name"	TEXT NOT NULL,
	"column_name"	TEXT NOT NULL,
	"color_back"	TEXT NOT NULL,
	"color_front"	TEXT NOT NULL,
	"color_hover"	TEXT NOT NULL,
	UNIQUE("table_name", "column_name"),
	PRIMARY KEY("config_id")
);
"""

import sqlite3
import uuid


class utils:
    connection = None

    def __init__(self):
        database = "database/garden.db"
        self.connection = sqlite3.connect(database)
        self.connection.execute("PRAGMA foreign_keys=on;")
        pass

    def __del__(self):
        self.connection.commit()
        self.connection.close()
        pass

    def guid(self) -> str:
        return str(uuid.uuid4()).upper()

    def table_exists(self, table="") -> bool:
        return False

    def create_table(self, table, columns=()):
        _COLUMNS = ",".join([f"`{column}` {datatype} NOT NULL" for column, datatype in columns])
        skeleton_sql = f"CREATE TABLE IF NOT EXISTS `{table}` ({_COLUMNS});"
        self.connection.execute(skeleton_sql)

    def columns_match(self, table="", config={}) -> bool:
        return False

    def get_tables(self):
        # skip config tables
        tables_sql = "select name from sqlite_master where type='table' AND name NOT LIKE 'config_%';";
        tables = self.connection.execute(tables_sql).fetchall()
        return tables

    def pragma_info(self, table):
        # print(f"PRAGMA TABLE_INFO(`{table}`);")
        return self.connection.execute(f"PRAGMA TABLE_INFO(`{table}`);").fetchall()

    def register_showfields(self, table, pragma=()):
        for c in pragma:
            insert_pragma = "INSERT OR IGNORE INTO config_showfields (config_id, table_name, column_name, column_datatype, showon_list, showon_edit, showon_detail, showon_insert, reserved_field) values(?, ?, ?, ?, ?, ?, ?, ?, ?);"
            cid, name, type, notnull, dflt_value, pk = c

            id = self.guid()
            table_name = table
            column_name = name
            column_datatype = type
            showon_list = 0
            showon_edit = 0
            showon_detail = 0
            showon_insert = 0
            reserved_field = 0
            data = (
                id, table_name, column_name, column_datatype, showon_list, showon_edit, showon_detail, showon_insert,
                reserved_field)
            # print(insert_pragma, data, sep="\r\n")
            self.connection.execute(insert_pragma, data)

    def register_colors(self, table, pragma=()):
        for c in pragma:
            insert_pragma = "INSERT OR IGNORE INTO config_colors (config_id, table_name, column_name, color_back, color_front, color_hover) VALUES (?, ?, ?, ?, ?, ?);"
            cid, name, type, notnull, dflt_value, pk = c

            id = self.guid()
            table_name = table
            column_name = name
            color_back = "#000000"
            color_front = "#FFFFFF"
            color_hover = "#F0F0F0"
            data = (id, table_name, column_name, color_back, color_front, color_hover)
            # print(insert_pragma, data, sep="\r\n")
            self.connection.execute(insert_pragma, data)


u = utils()
for table, columns in configs.items():
    if not u.table_exists(table):
        u.create_table(table, columns)
        # if not u.columns_match(table, columns):
        #    u.print_errors()

existing_tables = u.get_tables()
# print(existing_tables)
for row in existing_tables:
    # table_row[] is the table name
    table = row[0]
    pragma = u.pragma_info(table)
    u.register_showfields(table, pragma)
    u.register_colors(table, pragma)
    # print(pragma)
# CRUD table flag - for: config_showfields

print("Successful?")
