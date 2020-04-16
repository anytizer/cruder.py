# cruder.py

Python based CRUD Admin Panel Generator for Flask/SQLite web applications


## Configurations

`config.py` contains:
* Path to custom templates
* database name
* CRUD Entities
  * Table Name
  * Prefix Name
  * Entity name
  * list of hidden fields
  * List of extra fields


## Order of operation

- sqlite config.sql
- python builder.py
- python cruder.py > app.wsgi
- Restart your Flask Server: `python www.py`

## Considerations

- Each table has exactly one Primary Key Column, aka. ID
- Foreign Keys are handled at the database level
- run www.py as flask server
- Sorting? Field/asc/desc

Want to help? Read [ToDo](todo.md).