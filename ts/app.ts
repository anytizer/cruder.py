import uuid
from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

from entities.entity_{table} import entity_{table}


bp = Blueprint("BP_{table}", __name__, template_folder="templates", static_folder="static")


@bp.route("/{table}/", methods=["GET"])
def {table}_index():
    return redirect("/{table}/list")


@bp.route("/{table}/list/", methods=["GET"])
def {table}_list():
    entity = entity_{table}()
    data = entity.list()
    return render_template("/{table}/list.html", data=data)


@bp.route("/{table}/details/<{pk_id}>/", methods=["GET"])
def {table}_details({pk_id}):
    entity = entity_{table}()
    data = entity.details({pk_id})
    return render_template("/{table}/details.html", data=data)


@bp.route("/{table}/delete/<{pk_id}>/", methods=["GET"])
def {table}_delete({pk_id}):
    entity = entity_{table}()
    data = entity.delete({pk_id})
    return redirect("/{table}/list")


@bp.route("/{table}/add/", methods=["GET", "POST"])
def {table}_add():
    if request.method == "GET":
        return render_template("{table}/add.html", guid=str(uuid.uuid4()).upper())
    elif request.method == "POST":
        data = request.form
        entity = entity_{table}()
        entity.add(data)
        return redirect("/{table}/list", code=302)
    else:
        return "Not supported"


@bp.route("/{table}/edit/<{pk_id}>/", methods=["GET", "POST"])
def {table}_edit({pk_id}):
    if request.method == "GET":
        entity = entity_{table}()
        data = entity.details({pk_id})
        return render_template("/{table}/edit.html", data=data)
    elif request.method == "POST":
        data = request.form

        entity = entity_{table}()
        entity.update({pk_id}, data)

        return redirect("/{table}/list", code=302)
    else:
        return "Not supported"
