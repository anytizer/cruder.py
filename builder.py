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

# config.py:cruds
"""
DROP TABLE IF EXISTS config_tables;
CREATE TABLE "config_tables" (
	"table_id"	TEXT NOT NULL,
	"table_name"	TEXT NOT NULL,
    "table_prefix" TEXT NOT NULL,
    "pk_column" TEXT NOT NULL,
    "hidden_columns" TEXT NOT NULL,
    "extra_columns" TEXT NOT NULL,
    "do_crud"  TEXT NOT NULL,
    "child_column" TEXT NOT NULL,
    UNIQUE("table_name"),
    PRIMARY KEY("table_id")
);

DROP TABLE IF EXISTS config_showfields;
CREATE TABLE "config_showfields" (
	"config_id"	TEXT NOT NULL,
    "table_id" TEXT NOT NULL,
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
    "table_id" TEXT NOT NULL,
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
        tables_sql = "select name from sqlite_master where type='table' AND name NOT LIKE 'config_%';"
        tables = self.connection.execute(tables_sql).fetchall()
        return tables

    def table_id(self, table_name=""):
        sql="SELECT table_id FROM config_tables WHERE table_name=? LIMIT 1;"
        #print(sql)
        return self.connection.execute(sql, (table_name,)).fetchone()[0]

    def pragma_info(self, table):
        return self.connection.execute(f"PRAGMA TABLE_INFO(`{table}`);").fetchall()

    def register_table(self, table="") -> str:
        insert_table = "INSERT OR IGNORE INTO config_tables (table_id, table_name, table_prefix, pk_column, hidden_columns, extra_columns, do_crud, child_column) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
        table_prefix = ""
        pk_column = ""
        hidden_columns = ""
        extra_columns = ""
        do_crud = 1
        child_column = ""
        data = (self.guid(), table, table_prefix, pk_column, hidden_columns, extra_columns, do_crud, child_column)
        self.connection.execute(insert_table, data)
        return data[0]

    def register_showfields(self, table="", table_id="", pragma=()):
        for c in pragma:
            insert_pragma = "INSERT OR IGNORE INTO config_showfields (config_id, table_id, table_name, column_name, column_datatype, showon_list, showon_edit, showon_detail, showon_insert, reserved_field) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
            cid, name, type, notnull, dflt_value, pk = c

            id = self.guid()
            table_id = "" # @todo Calculate on...
            table_name = table
            column_name = name
            column_datatype = type
            showon_list = 0
            showon_edit = 0
            showon_detail = 0
            showon_insert = 0
            reserved_field = 0
            data = (
                id, table_id, table_name, column_name, column_datatype, showon_list, showon_edit, showon_detail, showon_insert,
                reserved_field)
            # print(insert_pragma, data, sep="\r\n")
            self.connection.execute(insert_pragma, data)

    def register_colors(self, table, table_id="", pragma=()):
        for c in pragma:
            insert_pragma = "INSERT OR IGNORE INTO config_colors (config_id, table_id, table_name, column_name, color_back, color_front, color_hover) VALUES (?, ?, ?, ?, ?, ?, ?);"
            cid, name, type, notnull, dflt_value, pk = c

            id = self.guid()
            table_name = table
            column_name = name
            color_back = "#000000"
            color_front = "#FFFFFF"
            color_hover = "#F0F0F0"
            data = (id, table_id, table_name, column_name, color_back, color_front, color_hover)
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
    # table_id = u.table_id(table)
    pragma = u.pragma_info(table)
    table_id = u.register_table(table)
    u.register_showfields(table, table_id, pragma)
    u.register_colors(table, table_id, pragma)
    # print(pragma)
# CRUD table flag - for: config_showfields

print("Successful?")
