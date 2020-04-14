from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

import meta
from database import database
from database import exporter


bp = Blueprint("BP_CUSTOM_ENDPOINTS", __name__, template_folder="templates", static_folder="static")


@bp.route("/config_showfields/flag/", methods=["POST"])
def config_showfields_flag():
    config_id = "AFE3BE75-6DD1-4E97-BBDC-08604E94600C"
    field =  request.form["field"]
    config_id = request.form["id"][0:36] # ID.FIELD_NAME
    query = f"""
update config_showfields set `{field}` = CASE `{field}` 
    WHEN '1' 
        THEN '0' 
    ELSE '1' 
END
where config_id=?;
    """
    e = exporter()
    e.query(query, (config_id,))
    return "Success?"
    #return "Something!"+field+", Query: "+query