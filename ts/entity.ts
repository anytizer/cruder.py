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

    def list(self, parent_id=""):
        # @todo filters should be in an array
        filters = ()
        select_query = "SELECT * FROM `{table}`;"
        if parent_id:
            filters = (parent_id,)
            select_query = "SELECT * FROM `{table}` WHERE `parent_id`=?;"

        data = self.query(select_query, filters)
        return data

    def search(self, parent_id="", query=""):
        # @todo To implement search
        # @todo filters should be in an array
        filters = ()
        search_query = "SELECT * FROM `{table}`;"
        data = self.query(search_query, filters)
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
        # delete_query = "UPDATE `{table}` SET is_deleted=1 WHERE `{pk_id}`=:{pk_id};"
        delete = self.query(delete_query, {"{pk_id}": {pk_id}})
        return delete

    def bulk(self, operation="", ids=()):
        # @todo To implement bulk operation on IDs
        return None
