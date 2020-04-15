import re

from flask import render_template, request, redirect
from flask import Blueprint

from tools.database import database


bp = Blueprint("BP_CUSTOM_ENDPOINTS", __name__, template_folder="templates", static_folder="static")


# from: configurator
@bp.route("/config_showfields/flag/", methods=["POST"])
def config_showfields_flag():
    field = re.sub(r'[^a-z0-9_]', '', request.form["field"]) # SQL Safety
    assert field == request.form["field"]
    assert field == request.form["id"][37:]
    # @see custom modified list.html
    config_id = request.form["id"][0:36] # ID.FIELD_NAME
    query = f"UPDATE config_showfields set `{field}`=CASE `{field}` WHEN '1' THEN '0' ELSE '1' END WHERE config_id=?;"
    db = database()
    db.query(query, (config_id,))
    return "Success?"


# @todo Apply for _v_ report views only
# Draw the list of columns and show the table contents
@bp.route("/optimized/<table_name>/", methods=["GET"])
def custom_table_name(table_name):
    table_name = re.sub(r'[^a-z0-9_]', '', table_name) 
    assert table_name != ""

    sql = f"""
-- List view SQL
SELECT sf.column_name cn, display_name dn FROM config_showfields sf
INNER JOIN config_tables t ON t.table_id = sf.table_id
WHERE
	t.table_name = ?
	AND sf.showon_list = ?
ORDER BY
    sf.display_order
;"""
    print(sql)
    db = database()

    columns_query = db.query(sql, (table_name, "1",))
    columns = ", ".join([f"`{column['cn']}`" for column in columns_query])
    heads = [column['dn'] for column in columns_query]
    assert columns != "", "Please choose at least few columns for this table to display."
    assert heads != [], "Cannot convert to Head Names."

    re_sql = f"SELECT {columns} FROM `{table_name}` LIMIT 10;"
    reports = db.query(re_sql, ())

    response = render_template("report-custom.html", reports=reports, columns=columns, heads=heads)
    return response


# from: gardens
@bp.route("/trays/showhide/<tray_id>/")
def trays_showhide(tray_id):
    db = database()
    db.query("UPDATE trays SET is_visible=CASE is_visible WHEN '1' THEN '0' ELSE '1' END WHERE tray_id=?;", (tray_id,))
    return redirect("/trays/list/")
