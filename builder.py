import json

from tools.meta import file_get_content
from tools.schema import schema
from tools.registrar import registrar


structure = json.loads(file_get_content("schema.json"))

s = schema()
for table, columns in structure.items():
    if not s.table_exists(table):
        s.create_table(table, columns)
        # if not u.columns_match(table, columns):
        #    u.print_errors()

r = registrar()
r.connection.executescript(file_get_content("config.sql"))
# print("Run config.sql manually.")

for row in s.get_tables():
    table = row[0]
    table_id = r.register_table(table)
    pragma = s.pragma_info(table)
    r.register_showfields(table_id, pragma)
    r.register_colors(table_id, pragma)

print("Successful?")
