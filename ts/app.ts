import os

import uuid
from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

from tools.meta import custom_template
from entities.entity_{table} import entity_{table}


bp = Blueprint("BP_{table}", __name__, template_folder="templates", static_folder="static")


@bp.route("/{table}/", methods=["GET"])
def {table}_index():
    return redirect(custom_template("/{table}/list"))


@bp.route("/{table}/bulk/", methods=["POST"])
def {table}_bulk():
    # @todo To implement bulk operation
    entity = entity_{table}()
    data = entity.bulk()
    return redirect(custom_template("/{table}/list.html"))


@bp.route("/{table}/list/", methods=["GET"], defaults={"parent_id": None})
@bp.route("/{table}/list/<parent_id>/", methods=["GET"])
def {table}_list(parent_id=None):
    entity = entity_{table}()
    data = entity.list(parent_id)
    return render_template(custom_template("/{table}/list.html"), data=data)


@bp.route("/{table}/search/", methods=["POST"], defaults={"parent_id": None})
@bp.route("/{table}/search/<parent_id>/", methods=["POST"])
def {table}_search(parent_id):
    entity = entity_{table}()
    query = request.form["query"]
    data = entity.search({"parent_id": parent_id}, query)
    return render_template(custom_template("/{table}/list.html"), data=data)


@bp.route("/{table}/details/<{pk_id}>/", methods=["GET"])
def {table}_details({pk_id}):
    entity = entity_{table}()
    data = entity.details({pk_id})
    return render_template(custom_template("/{table}/details.html"), data=data)


@bp.route("/{table}/delete/<{pk_id}>/", methods=["GET"])
def {table}_delete({pk_id}):
    entity = entity_{table}()
    data = entity.delete({pk_id})
    return redirect(custom_template("/{table}/list"))


@bp.route("/{table}/add/", methods=["GET", "POST"])
def {table}_add():
    if request.method == "GET":
        entity = entity_{table}()
        {LOOKUPS}
        return render_template(custom_template("{table}/add.html"), guid=str(uuid.uuid4()).upper(), {LOOKUPS_ASSIGNMENTS})
    elif request.method == "POST":
        data = request.form
        entity = entity_{table}()
        entity.add(data)
        return redirect(custom_template("/{table}/list"), code=302)
    else:
        return "Not supported"


@bp.route("/{table}/edit/<{pk_id}>/", methods=["GET", "POST"])
def {table}_edit({pk_id}):
    if request.method == "GET":
        entity = entity_{table}()
        data = entity.details({pk_id})
        return render_template(custom_template("/{table}/edit.html"), data=data)
    elif request.method == "POST":
        data = request.form
        entity = entity_{table}()
        entity.update({pk_id}, data)

        return redirect(custom_template("/{table}/list"), code=302)
    else:
        return "Not supported"
