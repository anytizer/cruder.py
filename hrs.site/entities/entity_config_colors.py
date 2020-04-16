import sqlite3
from flask import request, redirect
from database import database
import uuid


# entities/config_colors.py
class entity_config_colors(database):
    table = ""

    def __init__(self, table=""):
        super().__init__()
        self.table = table

    def list(self, parent_id=""):
        # @todo filters should be in an array
        filters = ()
        select_query = "SELECT * FROM `config_colors`;"
        if parent_id:
            filters = (parent_id,)
            select_query = "SELECT * FROM `config_colors` WHERE `parent_id`=?;"

        data = self.query(select_query, filters)
        return data

    def search(self, parent_id="", query=""):
        # @todo To implement search
        # @todo filters should be in an array
        filters = ()
        search_query = "SELECT * FROM `config_colors`;"
        data = self.query(search_query, filters)
        return data

    def add(self, data=[]):
        insert_query = """
            INSERT INTO `config_colors` (
                `config_id`, `table_id`, `column_name`, `color_back`, `color_front`, `color_hover`
            ) VALUES(
                :config_id, :table_id, :column_name, :color_back, :color_front, :color_hover
            );"""
        self.query(insert_query, data)

    def update(self, config_id="", data=[]):
        update_query = "UPDATE `config_colors` SET `config_id`=:config_id, `table_id`=:table_id, `column_name`=:column_name, `color_back`=:color_back, `color_front`=:color_front, `color_hover`=:color_hover WHERE `config_id`=:config_id;"
        self.query(update_query, data)

    def details(self, config_id=""):
        details_query = "SELECT * FROM `config_colors` WHERE `config_id`=:config_id LIMIT 1;"
        details = self.query(details_query, {"config_id": config_id})[0]
        return details

    def delete(self, config_id=""):
        delete_query = "DELETE FROM `config_colors` WHERE `config_id`=:config_id;"
        # delete_query = "UPDATE `config_colors` SET is_deleted=1 WHERE `config_id`=:config_id;"
        delete = self.query(delete_query, {"config_id": config_id})
        return delete

    def bulk(self, operation="", ids=()):
        # @todo To implement bulk operation on IDs
        return None
