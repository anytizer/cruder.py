import uuid
from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

from meta import T
from entities.entity_config_showfields import entity_config_showfields


bp = Blueprint("BP_config_showfields", __name__, template_folder="templates", static_folder="static")


@bp.route("/config_showfields/", methods=["GET"])
def config_showfields_index():
    return redirect(T("/config_showfields/list"))


@bp.route("/config_showfields/bulk/", methods=["POST"])
def config_showfields_bulk():
    # @todo To implement bulk operation
    entity = entity_config_showfields()
    data = entity.bulk()
    return redirect(T("/config_showfields/list.html"))


@bp.route("/config_showfields/list/", methods=["GET"], defaults={"parent_id": None})
@bp.route("/config_showfields/list/<parent_id>/", methods=["GET"])
def config_showfields_list(parent_id=None):
    entity = entity_config_showfields()
    data = entity.list(parent_id)
    return render_template(T("/config_showfields/list.html"), data=data)


@bp.route("/config_showfields/search/", methods=["POST"], defaults={"parent_id": None})
@bp.route("/config_showfields/search/<parent_id>/", methods=["POST"])
def config_showfields_search(parent_id):
    entity = entity_config_showfields()
    query = request.form["query"]
    data = entity.search({"parent_id": parent_id}, query)
    return render_template(T("/config_showfields/list.html"), data=data)


@bp.route("/config_showfields/details/<config_id>/", methods=["GET"])
def config_showfields_details(config_id):
    entity = entity_config_showfields()
    data = entity.details(config_id)
    return render_template(T("/config_showfields/details.html"), data=data)


@bp.route("/config_showfields/delete/<config_id>/", methods=["GET"])
def config_showfields_delete(config_id):
    entity = entity_config_showfields()
    data = entity.delete(config_id)
    return redirect(T("/config_showfields/list"))


@bp.route("/config_showfields/add/", methods=["GET", "POST"])
def config_showfields_add():
    if request.method == "GET":
        entity = entity_config_showfields()
        
        kv_table_ids_sql = "SELECT table_id k, table_name v FROM config_tables;"
        table_ids = entity.query(kv_table_ids_sql, ())
    
        return render_template(T("config_showfields/add.html"), guid=str(uuid.uuid4()).upper(), table_ids=table_ids)
    elif request.method == "POST":
        data = request.form
        entity = entity_config_showfields()
        entity.add(data)
        return redirect(T("/config_showfields/list"), code=302)
    else:
        return "Not supported"


@bp.route("/config_showfields/edit/<config_id>/", methods=["GET", "POST"])
def config_showfields_edit(config_id):
    if request.method == "GET":
        entity = entity_config_showfields()
        data = entity.details(config_id)
        return render_template(T("/config_showfields/edit.html"), data=data)
    elif request.method == "POST":
        data = request.form
        entity = entity_config_showfields()
        entity.update(config_id, data)

        return redirect(T("/config_showfields/list"), code=302)
    else:
        return "Not supported"
