# Running the Web-App:

Assumes a working Python 3 installation (with python=python3 and pip=pip3).

(1) Run the code below to install the dependencies.

>$ pip install -r requirements.txt

(2) Database initialization
1. set the database name in the __init__.py file.
2. run fill_tables.sql (fill_tables_mac.sql if used on macbook), create_tables.sql files in your database.

(3) Run Web-App
>$ python run.py

## Use 
In the "Economic graphs" tab the user can select two countries and an economic measure. 
After this the user selection will be submitted which will execute a sql-scripts extracting relevant data
Which will be plotted nicely for the user to analyze. 
This plot will be visualized to the user instant. 
