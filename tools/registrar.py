from tools.capitalizer import capitalize
from tools.database import database
from tools.provider import provider


# Registers configuration tables on a nominated database
class registrar(database):
    def __init__(self):
        super().__init__()

    def register_table(self, table="") -> str:
        table_prefix = ""
        pk_column = ""
        hidden_columns = ""
        extra_columns = ""
        do_crud = 1
        parent_column = ""

        insert_config = """
        INSERT OR IGNORE INTO config_tables (
        table_id, table_name, table_prefix, pk_column, hidden_columns, extra_columns, do_crud, parent_column
        ) VALUES(
            ?, ?, ?, ?, ?, ?, ?, ?
        );"""
        data = (provider().guid(), table, table_prefix, pk_column, hidden_columns, extra_columns, do_crud, parent_column)
        self.query(insert_config, data)

        # Do NOT return data[0] as table may not be created when exists already
        # Instead, query on the database
        table_id = self.query("SELECT table_id FROM config_tables WHERE table_name=? LIMIT 1;", (table, ))[0][0]
        return table_id

    def register_showfields(self, table_id="", pragma=()):
        display_order = 0
        for column in pragma:
            cid, name, type, notnull, dflt_value, pk = column

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
                provider().guid(), table_id, column_name, display_name, display_order, column_datatype, showon_list, showon_edit,
                showon_detail, showon_insert,
                reserved_field)
            self.query(insert_showfields, data)

    def register_colors(self, table_id="", pragma=()):
        for column in pragma:
            cid, name, type, notnull, dflt_value, pk = column

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
            data = (provider().guid(), table_id, column_name, color_back, color_front, color_hover)
            self.query(insert_colors, data)
