from flask import Response, render_template, request, redirect
from flask import Blueprint

from tools.database import exporter


bp = Blueprint("BP_COMMON_ENDPOINTS", __name__, template_folder="templates", static_folder="static")


@bp.route("/")
def index():
    return "It works!"


@bp.route("/import/<table>/", methods=["GET", "POST"])
def import_table_csv(table):
    if request.method == "GET":
        return render_template("import.html", table=table)
    elif request.method == "POST":
        e = exporter()
        e.importCSV(table, request.form["csv"])
        return redirect(f"/{table}/list/")
    else:
        return "Not supported"


@bp.route("/export/<table>/", methods=["GET"])
def export_table_csv(table):
    e = exporter()
    csv = e.export(table)
    response = Response(csv, mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename=f"{table}.csv")
    return response


@bp.route("/reports/<table>/", methods=["GET"])
def report(table):
    e = exporter()
    reports = e.report(table)
    response = render_template("report.html", reports=reports)
    return response
