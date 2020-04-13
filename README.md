# cruder.py
Python based CRUD Admin Panel Generator for Flask/SQLite applications

## Configurations
`config.py` contains the database name, and CRUD Entities (table name, prefix name, Entity name, list of hidden fields to apply)

## Running
`python cruder.py`
 
* Append the output into `www.py`.
* Restart the Flask Server


## Considerations
- Each table has exactly one Primary Key Column, aka. ID
- Foreign Keys are handled at the database level
- run www.py as flask server
- Sorting? Field/asc/desc
