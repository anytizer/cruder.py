import uuid
from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

from meta import T
from entities.entity_config_tables import entity_config_tables


bp = Blueprint("BP_config_tables", __name__, template_folder="templates", static_folder="static")


@bp.route("/config_tables/", methods=["GET"])
def config_tables_index():
    return redirect(T("/config_tables/list"))


@bp.route("/config_tables/bulk/", methods=["POST"])
def config_tables_bulk():
    # @todo To implement bulk operation
    entity = entity_config_tables()
    data = entity.bulk()
    return redirect(T("/config_tables/list.html"))


@bp.route("/config_tables/list/", methods=["GET"], defaults={"parent_id": None})
@bp.route("/config_tables/list/<parent_id>/", methods=["GET"])
def config_tables_list(parent_id=None):
    entity = entity_config_tables()
    data = entity.list(parent_id)
    return render_template(T("/config_tables/list.html"), data=data)


@bp.route("/config_tables/search/", methods=["POST"], defaults={"parent_id": None})
@bp.route("/config_tables/search/<parent_id>/", methods=["POST"])
def config_tables_search(parent_id):
    entity = entity_config_tables()
    query = request.form["query"]
    data = entity.search({"parent_id": parent_id}, query)
    return render_template(T("/config_tables/list.html"), data=data)


@bp.route("/config_tables/details/<table_id>/", methods=["GET"])
def config_tables_details(table_id):
    entity = entity_config_tables()
    data = entity.details(table_id)
    return render_template(T("/config_tables/details.html"), data=data)


@bp.route("/config_tables/delete/<table_id>/", methods=["GET"])
def config_tables_delete(table_id):
    entity = entity_config_tables()
    data = entity.delete(table_id)
    return redirect(T("/config_tables/list"))


@bp.route("/config_tables/add/", methods=["GET", "POST"])
def config_tables_add():
    if request.method == "GET":
        entity = entity_config_tables()
        
        return render_template(T("config_tables/add.html"), guid=str(uuid.uuid4()).upper(), )
    elif request.method == "POST":
        data = request.form
        entity = entity_config_tables()
        entity.add(data)
        return redirect(T("/config_tables/list"), code=302)
    else:
        return "Not supported"


@bp.route("/config_tables/edit/<table_id>/", methods=["GET", "POST"])
def config_tables_edit(table_id):
    if request.method == "GET":
        entity = entity_config_tables()
        data = entity.details(table_id)
        return render_template(T("/config_tables/edit.html"), data=data)
    elif request.method == "POST":
        data = request.form
        entity = entity_config_tables()
        entity.update(table_id, data)

        return redirect(T("/config_tables/list"), code=302)
    else:
        return "Not supported"
