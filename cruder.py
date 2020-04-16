from configs import config
import os
from tools import operations, meta

path = config.OUTPUT
os.makedirs(f"{path}/templates/__user__", 0x777, True)

inc_menu_html = " | ".join([f"<a href='/{table}/list'>{name}</a>" for table, prefix, name, hidden, extras in config.CRUDS])
inc_menu_html += " | <a href='/reports/reports'>Report</a>"
meta.write(f"{path}/templates/inc.menus.html", inc_menu_html)
meta.write(f"{path}/templates/base.html", meta.ts("ts/base.ts"))

config_body = operations.config()
config_body = config_body.replace("{OUTPUT}", config.OUTPUT)
meta.write(f"{path}/config.py", config_body)
print(f"""#!/bin/python
import sys
sys.path.insert(0, "d:/Desktop/cruder.py/cruder.py")

from apps import *

from flask import Flask
app = Flask(__name__)

""")

for table, prefix, name, hidden, extras in config.CRUDS:
    os.makedirs(f"{path}/templates/{table}/", 0x777, True)
    os.makedirs(f"{path}/entities/", 0x777, True)
    os.makedirs(f"{path}/apps/", 0x777, True)

    pk_id = meta.pk(table)
    columns = meta.columns(table)

    entity_template = operations.entity_body(table, columns, prefix, hidden, extras, pk_id)
    meta.write(f"{path}/entities/entity_{table}.py", entity_template)

    routes = operations.routes_body(table, columns, prefix, hidden, extras, pk_id)
    meta.write(f"{path}/apps/app_{table}.py", routes)

    list_html = operations.list_form(table, columns, prefix, hidden, extras, pk_id)
    meta.write(f"{path}/templates/{table}/list.html", list_html)

    add_form_html = operations.add_form(table, columns, prefix, hidden, extras, pk_id)
    meta.write(f"{path}/templates/{table}/add.html", add_form_html)

    edit_html = operations.edit_form(table, columns, prefix, hidden, extras, pk_id)
    meta.write(f"{path}/templates/{table}/edit.html", edit_html)

    details_html = operations.details_form(table, columns, prefix, hidden, extras, pk_id)
    meta.write(f"{path}/templates/{table}/details.html", details_html)

    print(f"app.register_blueprint(app_{table}.bp)")
# touch /templates/entity/{list.html,edit.html,add.html}
web = """
app.register_blueprint(app_common.bp)
app.register_blueprint(app_custom.bp)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
"""
print(web)
