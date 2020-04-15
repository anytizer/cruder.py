import re

from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

import meta
from database import database


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
    sql = f"""
-- List view SQL
SELECT sf.column_name cn FROM config_showfields sf
INNER JOIN config_tables t ON t.table_id = sf.table_id
WHERE
	t.table_name = '{table_name}'
	AND sf.showon_list = '1'
;"""
    db = database()

    columns = ", ".join([f"`{column['cn']}`" for column in db.query(sql)])
    re_sql = f"SELECT {columns} FROM `{table_name}` LIMIT 10;"
    print(columns, re_sql)
    #return "That!"
    reports = db.query(re_sql, ())
    response = render_template("report-custom.html", reports=reports)
    return response


# from: gardens
@bp.route("/trays/showhide/<tray_id>/")
def trays_showhide(tray_id):
    db = database()
    db.query("UPDATE trays SET is_visible=CASE is_visible WHEN '1' THEN '0' ELSE '1' END WHERE tray_id=?;", (tray_id,))
    return redirect("/trays/list/")
