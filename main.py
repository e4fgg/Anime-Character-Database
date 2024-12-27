# Making a program that is connected to a Postgres SQL Server where the user is able to insert data into the server with their input.
# Date: December 26, 2024
# MacOS Sonoma / Python 3.12
# main.py

# Importing the module that connects the Postgres SQL Server to Python.
import psycopg2

#############################
#                           #
#      SERVER DETAILS       #
#                           #
#############################

# Database was already created in another file named create.sql that is in this repository.
# Opening a cursor.
cur = connect.cursor()

# Class that will store methods.
class Database:
    def __init__(self):
        pass

    # Defining a method that will make it possible to insert data into database.
    def insert(self):
        # Asks users for how many records (rows) they would like to contribute to.
        records = int(input("How many rows would you like to insert: "))

        