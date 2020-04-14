from flask import Flask, Response, render_template, request, redirect
from flask import Blueprint

import meta
from database import database


bp = Blueprint("BP_CSV_IMPORT_EXPORT", __name__, template_folder="templates", static_folder="static")


class exporter(database):
    def export(self, table=""):
        export_query = f"SELECT * FROM `{table}` LIMIT 5000;"
        csv = self.query(export_query, ())
        columns = meta.columns(table)

        _csv = ["\t".join([f"{column}" for column in columns])]
        for r in csv:
            try:
                values = "\t".join(f"{str(column)}" for column in dict(r).values())
                _csv.append(values)
            except ValueError:
                pass
        return "\r\n".join(_csv)

    def importCSV(self, table="", csv="") -> bool:
        # for lines, import csv
        # self.query()
        return True

    def report(self, view_table="reports"):
        # @todo safeguard the variable
        # @todo _v_ attached. Other characters to be replaced
        records = self.query(f"SELECT * FROM `_v_{view_table}`")
        return records


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
    # print(reports)
    response = render_template("report.html", reports=reports)
    return response
