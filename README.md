# twitt_off_hw

A web application to add books into the table.

# STEPS

1. Created pip enviroment with Flask, Flask-SQLAlchemy, Flask-Migrate installed

2. Created main project directory ("twitt_off"), where I placed routes directery with "routes.py" in it (to specify routes), __init__.py, twitt_off.py

3. Created book_routes.py

4. Created HTML file, used jinja to insert dynamic contents into the HTML

5. In a file models.py, define a class to create books instances

6. Initialize the db: 
'''sh
FLASK_APP=twitt_off flask db init # generates app/migrations dir

FLASK_APP=twitt_off flask db migrate # creates db

FLASK_APP=twitt_off flask db upgrade # create specified tables
'''

