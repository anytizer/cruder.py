import hashlib
import sqlite3
from os import path

import config
import _capitalizer


# Return user templates from within __user__ dir
def T(requested_template="") -> str:
    user_template = config.template + "/" + requested_template.lstrip("/")
    if path.isfile(user_template):
        requested_template = "__user__/" + requested_template.lstrip("/")
    #print("Template request: "+requested_template, "Searching: ", user_template)
    return requested_template


def columns(table):
    connection = sqlite3.connect(config.database)
    cursor = connection.cursor()

    info_sql = f"PRAGMA TABLE_INFO('{table}');"
    resource = cursor.execute(info_sql, ())
    data = resource.fetchall()
    # cid, name, type, notnull, dflt_value, pk
    cols = [c[1] for c in data]
    connection.commit()
    connection.close()
    return cols


def pk(table):
    connection = sqlite3.connect(config.database)
    cursor = connection.cursor()

    info_sql = f"PRAGMA TABLE_INFO('{table}');"
    resource = cursor.execute(info_sql, ())
    data = resource.fetchall()
    pk_column = ""
    for cid, name, type, notnull, dflt_value, pk in data:
        if pk == 1:
            pk_column = name
    connection.commit()
    connection.close()
    return pk_column


# Column Head Name. Eg. ID for customer_id.
def headname(column="", prefix=""):
    hn = column.replace(prefix, "").title()
    hn = " ".join([_capitalizer.capitalize(word) for word in hn.split("_")])
    return hn


def href(table="", field={}, pk_id=""):
    # "/close/<>" => "/table/close/{{data.pk_id}}"
    # field['url'] = field['url'].lower().lstrip("/")
    field['url'] = field['url'].replace("/<>", f"/{{{{ data.{pk_id} }}}}")
    # field['url'] = "/" + table + "/" + field['url']
    link = f"<a class='w3-btn w3-purple' href='{field['url']}'>{headname(field['column'])}</a>"
    return link


def ts(filename="") -> str:
    template = str(open(filename, "r").read())
    return template


def write(filename="", content=""):
    with open(filename, "w") as fp:
        fp.write(content)


def encrypt(field=""):
    return field
#    _hash = "H"+hashlib.sha256(field.encode()).hexdigest().upper()
#    return _hash

