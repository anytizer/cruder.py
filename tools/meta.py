import sqlite3
from os import path

from configs import config
from tools import capitalizer
from tools.database import database


def file_get_content(file=""):
    content = ""
    with open(file) as f:
        content = f.read()
    return content

# Return user templates from within templates/__user__/ dir
# Do NOT CRUD under name: __user__


def custom_template(requested_template="") -> str:
    user_template = config.CUSTOM_TEMPLATE.rstrip("/") + "/" + requested_template.lstrip("/")
    if path.isfile(user_template):
        requested_template = "__user__/" + requested_template.lstrip("/")
    # print("Template request: "+requested_template, "Searching: ", user_template)
    return requested_template


def columns(table):
    db = database()
    info_sql = f"PRAGMA TABLE_INFO('{table}');"
    cols = [c[1] for c in db.connection.execute(info_sql).fetchall()]
    return cols


def pk(table):
    connection = sqlite3.connect(config.DATABASE)
    cursor = connection.cursor()

    info_sql = f"PRAGMA TABLE_INFO(`{table}`);"
    resource = cursor.execute(info_sql, ())
    data = resource.fetchall()
    pk_column = ""
    for cid, name, type, notnull, dflt_value, pk in data:
        if pk == 1:
            pk_column = name
    assert pk_column != "", "Primary key not found in this table"
    return pk_column


# Column Head Name. Eg. ID for customer_id.
def headname(column="", prefix=""):
    hn = column.replace(prefix, "").title()
    hn = " ".join([capitalizer.capitalize(word) for word in hn.split("_")])
    return hn


def href(table="", field={}, pk_id=""):
    # "/close/<>" => "/table/close/{{data.pk_id}}"
    field['url'] = field['url'].replace("/<>", f"/{{{{ data.{pk_id} }}}}")
    link = f"<a class='w3-btn w3-purple' href='{field['url']}'>{headname(field['column'])}</a>"
    return link


def ts(filename="") -> str:
    template = str(open(filename, "r").read())
    return template


def write(filename="", content=""):
    with open(filename, "w") as fp:
        fp.write(content)


def encrypt(field=""):
    _hash = field
    # Should NOT start with numbers
    # _hash = "H"+hashlib.sha256(field.encode()).hexdigest().upper()
    return _hash
