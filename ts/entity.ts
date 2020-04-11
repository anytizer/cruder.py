import sqlite3
from flask import request, redirect
from database import database
import uuid


# entities/{table}.py
class entity_{table}(database):
    table = ""

    def __init__(self, table=""):
        super().__init__()
        self.table = table

    def list(self):
        select_query = "SELECT * FROM `{table}`;"
        data = self.query(select_query)
        return data

    def add(self, data=[]):
        insert_query = """{insert_query}"""
        self.query(insert_query, data)

    def update(self, {pk_id}="", data=[]):
        update_query = "{update_query}"
        self.query(update_query, data)

    def details(self, {pk_id}=""):
        details_query = "SELECT * FROM `{table}` WHERE `{pk_id}`=:{pk_id} LIMIT 1;"
        details = self.query(details_query, {"{pk_id}": {pk_id}})[0]
        return details

    def delete(self, {pk_id}=""):
        delete_query = "DELETE FROM `{table}` WHERE `{pk_id}`=:{pk_id};"
        delete = self.query(delete_query, {"{pk_id}": {pk_id}})
        return delete
