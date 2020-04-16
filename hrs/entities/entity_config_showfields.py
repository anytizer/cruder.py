import sqlite3
from flask import request, redirect
from tools.database import database
import uuid


# entities/config_showfields.py
class entity_config_showfields(database):
    table = ""

    def __init__(self, table=""):
        super().__init__()
        self.table = table

    def list(self, parent_id=""):
        # @todo filters should be in an array
        filters = ()
        select_query = "SELECT * FROM `config_showfields`;"
        if parent_id:
            filters = (parent_id,)
            select_query = "SELECT * FROM `config_showfields` WHERE `parent_id`=?;"

        data = self.query(select_query, filters)
        return data

    def search(self, parent_id="", query=""):
        # @todo To implement search
        # @todo filters should be in an array
        filters = ()
        search_query = "SELECT * FROM `config_showfields`;"
        data = self.query(search_query, filters)
        return data

    def add(self, data=[]):
        insert_query = """
            INSERT INTO `config_showfields` (
                `config_id`, `table_id`, `column_name`, `display_name`, `display_order`, `column_datatype`, `showon_list`, `showon_edit`, `showon_detail`, `showon_insert`, `reserved_field`
            ) VALUES(
                :config_id, :table_id, :column_name, :display_name, :display_order, :column_datatype, :showon_list, :showon_edit, :showon_detail, :showon_insert, :reserved_field
            );"""
        self.query(insert_query, data)

    def update(self, config_id="", data=[]):
        update_query = "UPDATE `config_showfields` SET `config_id`=:config_id, `table_id`=:table_id, `column_name`=:column_name, `display_name`=:display_name, `display_order`=:display_order, `column_datatype`=:column_datatype, `showon_list`=:showon_list, `showon_edit`=:showon_edit, `showon_detail`=:showon_detail, `showon_insert`=:showon_insert, `reserved_field`=:reserved_field WHERE `config_id`=:config_id;"
        self.query(update_query, data)

    def details(self, config_id=""):
        details_query = "SELECT * FROM `config_showfields` WHERE `config_id`=:config_id LIMIT 1;"
        details = self.query(details_query, {"config_id": config_id})[0]
        return details

    def delete(self, config_id=""):
        delete_query = "DELETE FROM `config_showfields` WHERE `config_id`=:config_id;"
        # delete_query = "UPDATE `config_showfields` SET is_deleted=1 WHERE `config_id`=:config_id;"
        delete = self.query(delete_query, {"config_id": config_id})
        return delete

    def bulk(self, operation="", ids=()):
        # @todo To implement bulk operation on IDs
        return None
