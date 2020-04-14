from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

import meta
from database import database
from database import exporter


bp = Blueprint("BP_CUSTOM_ENDPOINTS", __name__, template_folder="templates", static_folder="static")


# from: configurator
@bp.route("/config_showfields/flag/", methods=["POST"])
def config_showfields_flag():
    field =  request.form["field"]
    config_id = request.form["id"][0:36] # ID.FIELD_NAME
    query = f"UPDATE config_showfields set `{field}` = CASE `{field}` WHEN '1' THEN '0' ELSE '1' END WHERE config_id=?;"
    e = exporter()
    e.query(query, (config_id,))
    return "Success?"


# from: gardens
@bp.route("/trays/showhide/<tray_id>/")
def trays_showhide(tray_id):
    e = exporter()
    e.query("UPDATE trays SET is_visible=CASE is_visible WHEN '1' THEN '0' ELSE '1' END WHERE tray_id=?;", (tray_id,))
    return redirect("/trays/list/")
