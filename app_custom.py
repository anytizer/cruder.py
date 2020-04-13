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

    def report(self, _v_view_table="reports"):
        db = database()
        records = db.query(f"SELECT * FROM `{_v_view_table}`")
        return records


@bp.route("/")
def index():
    return "It works!"


@bp.route("/export/<table>/", methods=["GET"])
def csv_index(table):
    e = exporter()
    csv = e.export(table)
    response = Response(csv, mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename=f"{table}.csv")
    return response


@bp.route("/report/<table>/", methods=["GET"])
def report(table):
    e = exporter()
    reports = e.report(table)
    print(reports)
    response = render_template("report.html", reports=reports)
    return response
