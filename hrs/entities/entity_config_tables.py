import sqlite3
from flask import request, redirect
from tools.database import database
import uuid


# entities/config_tables.py
class entity_config_tables(database):
    table = ""

    def __init__(self, table=""):
        super().__init__()
        self.table = table

    def list(self, parent_id=""):
        # @todo filters should be in an array
        filters = ()
        select_query = "SELECT * FROM `config_tables`;"
        if parent_id:
            filters = (parent_id,)
            select_query = "SELECT * FROM `config_tables` WHERE `parent_id`=?;"

        data = self.query(select_query, filters)
        return data

    def search(self, parent_id="", query=""):
        # @todo To implement search
        # @todo filters should be in an array
        filters = ()
        search_query = "SELECT * FROM `config_tables`;"
        data = self.query(search_query, filters)
        return data

    def add(self, data=[]):
        insert_query = """
            INSERT INTO `config_tables` (
                `table_id`, `table_name`, `table_prefix`, `pk_column`, `hidden_columns`, `extra_columns`, `do_crud`, `parent_column`
            ) VALUES(
                :table_id, :table_name, :table_prefix, :pk_column, :hidden_columns, :extra_columns, :do_crud, :parent_column
            );"""
        self.query(insert_query, data)

    def update(self, table_id="", data=[]):
        update_query = "UPDATE `config_tables` SET `table_id`=:table_id, `table_name`=:table_name, `table_prefix`=:table_prefix, `pk_column`=:pk_column, `hidden_columns`=:hidden_columns, `extra_columns`=:extra_columns, `do_crud`=:do_crud, `parent_column`=:parent_column WHERE `table_id`=:table_id;"
        self.query(update_query, data)

    def details(self, table_id=""):
        details_query = "SELECT * FROM `config_tables` WHERE `table_id`=:table_id LIMIT 1;"
        details = self.query(details_query, {"table_id": table_id})[0]
        return details

    def delete(self, table_id=""):
        delete_query = "DELETE FROM `config_tables` WHERE `table_id`=:table_id;"
        # delete_query = "UPDATE `config_tables` SET is_deleted=1 WHERE `table_id`=:table_id;"
        delete = self.query(delete_query, {"table_id": table_id})
        return delete

    def bulk(self, operation="", ids=()):
        # @todo To implement bulk operation on IDs
        return None
