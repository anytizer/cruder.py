import sqlite3
from flask import request, redirect
from tools.database import database
import uuid


# entities/employees.py
class entity_employees(database):
    table = ""

    def __init__(self, table=""):
        super().__init__()
        self.table = table

    def list(self, parent_id=""):
        # @todo filters should be in an array
        filters = ()
        select_query = "SELECT * FROM `employees`;"
        if parent_id:
            filters = (parent_id,)
            select_query = "SELECT * FROM `employees` WHERE `parent_id`=?;"

        data = self.query(select_query, filters)
        return data

    def search(self, parent_id="", query=""):
        # @todo To implement search
        # @todo filters should be in an array
        filters = ()
        search_query = "SELECT * FROM `employees`;"
        data = self.query(search_query, filters)
        return data

    def add(self, data=[]):
        insert_query = """
            INSERT INTO `employees` (
                `employee_id`, `employee_name`, `employee_firstname`, `employee_lastname`, `employee_address`, `employee_phone`
            ) VALUES(
                :employee_id, :employee_name, :employee_firstname, :employee_lastname, :employee_address, :employee_phone
            );"""
        self.query(insert_query, data)

    def update(self, employee_id="", data=[]):
        update_query = "UPDATE `employees` SET `employee_id`=:employee_id, `employee_name`=:employee_name, `employee_firstname`=:employee_firstname, `employee_lastname`=:employee_lastname, `employee_address`=:employee_address, `employee_phone`=:employee_phone WHERE `employee_id`=:employee_id;"
        self.query(update_query, data)

    def details(self, employee_id=""):
        details_query = "SELECT * FROM `employees` WHERE `employee_id`=:employee_id LIMIT 1;"
        details = self.query(details_query, {"employee_id": employee_id})[0]
        return details

    def delete(self, employee_id=""):
        delete_query = "DELETE FROM `employees` WHERE `employee_id`=:employee_id;"
        # delete_query = "UPDATE `employees` SET is_deleted=1 WHERE `employee_id`=:employee_id;"
        delete = self.query(delete_query, {"employee_id": employee_id})
        return delete

    def bulk(self, operation="", ids=()):
        # @todo To implement bulk operation on IDs
        return None
