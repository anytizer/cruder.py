from tools.builder_utils import builder_utils
from tools.registrar import registrar

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

u = builder_utils()
for table, columns in configs.items():
    if not u.table_exists(table):
        u.create_table(table, columns)
        # if not u.columns_match(table, columns):
        #    u.print_errors()

r = registrar()
for row in u.get_tables():
    table = row[0]
    table_id = r.register_table(table)
    pragma = u.pragma_info(table)
    r.register_showfields(table_id, pragma)
    r.register_colors(table_id, pragma)

print("Successful?")
