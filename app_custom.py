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
    query = f"UPDATE config_showfields set `{field}` = CASE `{field}` WHEN '1' THEN '0' ELSE '1' END WHERE config_id=?;"
    db = database()
    db.query(query, (config_id,))
    return "Success?"


# from: gardens
@bp.route("/trays/showhide/<tray_id>/")
def trays_showhide(tray_id):
    db = database()
    db.query("UPDATE trays SET is_visible=CASE is_visible WHEN '1' THEN '0' ELSE '1' END WHERE tray_id=?;", (tray_id,))
    return redirect("/trays/list/")
