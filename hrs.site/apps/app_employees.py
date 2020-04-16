import uuid
from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

from meta import T
from entities.entity_employees import entity_employees


bp = Blueprint("BP_employees", __name__, template_folder="templates", static_folder="static")


@bp.route("/employees/", methods=["GET"])
def employees_index():
    return redirect(T("/employees/list"))


@bp.route("/employees/bulk/", methods=["POST"])
def employees_bulk():
    # @todo To implement bulk operation
    entity = entity_employees()
    data = entity.bulk()
    return redirect(T("/employees/list.html"))


@bp.route("/employees/list/", methods=["GET"], defaults={"parent_id": None})
@bp.route("/employees/list/<parent_id>/", methods=["GET"])
def employees_list(parent_id=None):
    entity = entity_employees()
    data = entity.list(parent_id)
    return render_template(T("/employees/list.html"), data=data)


@bp.route("/employees/search/", methods=["POST"], defaults={"parent_id": None})
@bp.route("/employees/search/<parent_id>/", methods=["POST"])
def employees_search(parent_id):
    entity = entity_employees()
    query = request.form["query"]
    data = entity.search({"parent_id": parent_id}, query)
    return render_template(T("/employees/list.html"), data=data)


@bp.route("/employees/details/<employee_id>/", methods=["GET"])
def employees_details(employee_id):
    entity = entity_employees()
    data = entity.details(employee_id)
    return render_template(T("/employees/details.html"), data=data)


@bp.route("/employees/delete/<employee_id>/", methods=["GET"])
def employees_delete(employee_id):
    entity = entity_employees()
    data = entity.delete(employee_id)
    return redirect(T("/employees/list"))


@bp.route("/employees/add/", methods=["GET", "POST"])
def employees_add():
    if request.method == "GET":
        entity = entity_employees()
        
        return render_template(T("employees/add.html"), guid=str(uuid.uuid4()).upper(), )
    elif request.method == "POST":
        data = request.form
        entity = entity_employees()
        entity.add(data)
        return redirect(T("/employees/list"), code=302)
    else:
        return "Not supported"


@bp.route("/employees/edit/<employee_id>/", methods=["GET", "POST"])
def employees_edit(employee_id):
    if request.method == "GET":
        entity = entity_employees()
        data = entity.details(employee_id)
        return render_template(T("/employees/edit.html"), data=data)
    elif request.method == "POST":
        data = request.form
        entity = entity_employees()
        entity.update(employee_id, data)

        return redirect(T("/employees/list"), code=302)
    else:
        return "Not supported"
