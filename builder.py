from tools.schema import schema
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

s = schema()
for table, columns in configs.items():
    if not s.table_exists(table):
        s.create_table(table, columns)
        # if not u.columns_match(table, columns):
        #    u.print_errors()

r = registrar()
with open("config.sql") as f:
    config_sql = f.read()
    r.connection.executescript(config_sql)
print("Run config.sql manually.")

for row in s.get_tables():
    table = row[0]
    table_id = r.register_table(table)
    pragma = s.pragma_info(table)
    r.register_showfields(table_id, pragma)
    r.register_colors(table_id, pragma)

print("Successful?")
