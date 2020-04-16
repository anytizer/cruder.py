output = "hrs/"
template_custom = "hrs/templates/__user__/"
database = "hrs/database/hrs.db"
cruds = (
    ("employees", "employee_", "Employees", (), ()),
    ("config_tables", "", "Tables", (), (
        {"column": "Fields", "url": "/config_showfields/list/<>"},
    )),
    ("config_colors", "", "Colors", (), ()),
    ("config_showfields", "", "Fields", (
        {"column": "table_id", "sql": "SELECT table_id k, table_name v FROM config_tables;"},
    ), ()),
)
