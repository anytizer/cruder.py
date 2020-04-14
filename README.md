# cruder.py
Python based CRUD Admin Panel Generator for Flask/SQLite applications

## Configurations
`config.py` contains the database name, and CRUD Entities (table name, prefix name, Entity name, list of hidden fields to apply)
 
* Append the output into `www.py`.
* Restart your Flask Server.

## Order of operation
- python builder.py
- python crduer.py
- python www.py

## Considerations
- Each table has exactly one Primary Key Column, aka. ID
- Foreign Keys are handled at the database level
- run www.py as flask server
- Sorting? Field/asc/desc
