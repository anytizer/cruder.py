database_file = "database.db"

# table, prefix, name, hidden=[], list view cols=[]
cruds = [
    ("artworks", "artwork_", "Artworks", ["project_id"], ["accept"]),
    ("customers", "customer_", "Customers", [], ["accept"]),
    ("developers", "developer_", "Developers", [], []),
    ("estimations", "estimation_", "Estimations", ['project_id'], []),
    ("payments", "payment_", "Payments", ['project_id'], []),
    ("projects", "project_", "Projects", ['customer_id'], []),
    ("terminations", "termination_", "Terminations", ['project_id'], []),
    ("works", "work_", "Works", [], []),
    ("info", "info_", "Information", [], []),
]

# each table has exactly one PK ID
