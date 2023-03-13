
import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database=db_name
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error {err}")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: {err}")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: {err}")


#Queries
create_database_query = "create database EXOTIC_DEALERSHIP"


#create coupe table
create_coupe_table = """  
create table COUPE_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL);"""

#create suv table
create_suv_table = """
create table SUV_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL);
"""

#populate coupe table
coupe_vehicles = """ 
insert into COUPE_MODELS values
('123abc321','Ashton Martin', 'Vanquish', 200, 115000),
('asd748541', 'Audi', 'RS 7', 1200, 12500) """

#calling statement
connection = create_server_connection("localhost", "root", "student","exotic_dealership")
#call work horse function to run query
execute_query(connection, coupe_vehicles )

