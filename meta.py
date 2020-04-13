import hashlib
import sqlite3

from config import database_file
# from config import table


def columns(table):
    connection = sqlite3.connect(database_file)
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
    connection = sqlite3.connect(database_file)
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
    hn = hn.replace("_", " ")
    return hn


def href(table="", field={}, pk_id=""):
    # url = "/close/<>"
    field['url'] = field['url'].lower().lstrip("/")
    field['url'] = field['url'].replace("/<>", f"/{{{{ data.{pk_id} }}}}")
    field['url'] = "/" + table + "/" + field['url']
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
