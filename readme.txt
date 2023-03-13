
Install Extensions:


Configuration:
    - Installation of extensions:
    -mysql
    -mysql-connector
    -mysql-connector-python
    - pandas - pandas is a software library written for the Python
    programming language
    for data manipulation and analysis. In particular, it offers
    data structures and operations for
    manipulating numerical tables and time series.

file>settings>name of project > project interpreter, search each extension then
install

Establish communication to mysql

1.) Content for main.py.
-establish connection from code window to mysql
content for main.py:

import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error {err}")
    return connection
#calling statement
connection = create_server_connection("localhost", "root", "student")


2.) Creation of database.
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: {err}")
#Queries
create_database_query = "create database EXOTIC_DEALERSHIP"
#calling statement
connection = create_server_connection("localhost", "root", "student")
#call create_database function to create DB in mySQL
create_database(connection, create_database_query)


3.) Add database name to "create_server_connection" function and calling statement

def create_server_connection(host_name, user_name, user_password, db_name): <------ add db_name
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name   <----- assign argument
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error {err}")
    return connection
connection = create_server_connection("localhost", "root", "student","exotic_dealership") <-- place DB name

4.) Place work horse function to run queries:

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: {err}")

5.) create sql query to create coupe table in DB.

#create coupe table
create_coupe_table = """
create table COUPE_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL);"""

execute_query(connection, create_coupe_table )

6.) create sql query to create SUV table in DB.

#create suv table
create_suv_table = """
create table SUV_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL);
"""
#calling statement using work horse function:
execute_query(connection, create_suv_table )

7.) populate coupe table:


#populate coupe table
coupe_vehicles = """ < ----- create variable to hold query
insert into COUPE_MODELS values
('123abc321','Ashton Martin', 'Vanquish', 200, 115000),
('asd748541', 'Audi', 'RS 7', 1200, 12500) """  <--- end of value

execute_query(connection, coupe_vehicles ) <---- calling statement.


8.) populate SUV table:

#populate suv table
suv_table = """
insert into SUV_MODELS values
('123abc321','Lamborghini', 'Urus', 787, 135000),
('asd748541', 'BMW', 'X5', 1200, 12500) """
#calling statement
execute_query(connection, suv_table)




