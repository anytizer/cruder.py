import uuid
from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

from meta import T
from entities.entity_config_colors import entity_config_colors


bp = Blueprint("BP_config_colors", __name__, template_folder="templates", static_folder="static")


@bp.route("/config_colors/", methods=["GET"])
def config_colors_index():
    return redirect(T("/config_colors/list"))


@bp.route("/config_colors/bulk/", methods=["POST"])
def config_colors_bulk():
    # @todo To implement bulk operation
    entity = entity_config_colors()
    data = entity.bulk()
    return redirect(T("/config_colors/list.html"))


@bp.route("/config_colors/list/", methods=["GET"], defaults={"parent_id": None})
@bp.route("/config_colors/list/<parent_id>/", methods=["GET"])
def config_colors_list(parent_id=None):
    entity = entity_config_colors()
    data = entity.list(parent_id)
    return render_template(T("/config_colors/list.html"), data=data)


@bp.route("/config_colors/search/", methods=["POST"], defaults={"parent_id": None})
@bp.route("/config_colors/search/<parent_id>/", methods=["POST"])
def config_colors_search(parent_id):
    entity = entity_config_colors()
    query = request.form["query"]
    data = entity.search({"parent_id": parent_id}, query)
    return render_template(T("/config_colors/list.html"), data=data)


@bp.route("/config_colors/details/<config_id>/", methods=["GET"])
def config_colors_details(config_id):
    entity = entity_config_colors()
    data = entity.details(config_id)
    return render_template(T("/config_colors/details.html"), data=data)


@bp.route("/config_colors/delete/<config_id>/", methods=["GET"])
def config_colors_delete(config_id):
    entity = entity_config_colors()
    data = entity.delete(config_id)
    return redirect(T("/config_colors/list"))


@bp.route("/config_colors/add/", methods=["GET", "POST"])
def config_colors_add():
    if request.method == "GET":
        entity = entity_config_colors()
        
        return render_template(T("config_colors/add.html"), guid=str(uuid.uuid4()).upper(), )
    elif request.method == "POST":
        data = request.form
        entity = entity_config_colors()
        entity.add(data)
        return redirect(T("/config_colors/list"), code=302)
    else:
        return "Not supported"


@bp.route("/config_colors/edit/<config_id>/", methods=["GET", "POST"])
def config_colors_edit(config_id):
    if request.method == "GET":
        entity = entity_config_colors()
        data = entity.details(config_id)
        return render_template(T("/config_colors/edit.html"), data=data)
    elif request.method == "POST":
        data = request.form
        entity = entity_config_colors()
        entity.update(config_id, data)

        return redirect(T("/config_colors/list"), code=302)
    else:
        return "Not supported"
