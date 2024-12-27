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

        # For each of the numbers that the user entered for the records variable, it will loop.
        for record in records:
            # Keeping count.
            print(f"Row #{record} out of {records}:")

            # Prompts user to enter character's English name.
            eng_name = input("Please enter character's English name: ")

            # Prompts user to enter character's Japanese name.
            japa_name = input("Please enter character's Japanese name: ")

            # Prompts user to enter character's birthday.
            birthday = input("Please enter character's birthday: ")

            # Prompts user to enter the anime that the character is in.
            anime = input("Please enter the anime this character is in: ")

            # Executes the INSERT Statement.
            cur.execute("INSERT INTO usercharacters.characters (EnglishName, JapaneseName, Birthday, Anime) VALUES (%s, %s, %s, %s)",
            (eng_name, japa_name, birthday, anime)) # The values that the user entered will be added into the database, the ID is auto-generated.

            # Makes changes to the actual database.
            connect.commit()

            # Lets user know that the changes migrated to the database.
            print("All changes have been made to the database! ✅")

        # Closing database and cursor.
        connect.close()
        cur.close()

    # The method that allows user to view all records in the database.
    def view(self):
        cur.execute("SELECT * FROM usercharacters.Characters;") # Selecting all records to view.

        print(cur.fetchall()) # Printing all the records.

        # Closing database and cursor.
        connect.close()
        cur.close()

    # Method that allows user to search for a certain character based on character's name.
    def search(self):
        # Program prompts user for the character's id.
        user_search = input("Please enter the id of character: ")

        # SQL Command.
        cur.execute(f"SELECT * FROM usercharacters.Characters WHERE CharacterID = {user_search}")

        # Printing the results.
        print(cur.fetchall())

        # Closing database and cursor.
        connect.close()
        cur.close()

    # Method that allows user to update data about a character.
    def update(self):
        # Program prompts user for the character's id.
        id_search = input("Please enter the id of character: ")

        # Program prompts user for the number of columns they would like to update.
        columns = input("Please enter the number of you would like to update: ")

        # Input validation.
        while not (columns <= 5 and columns.isdigit()):
            input("Please make sure the number you entered is between 1 and 5, please try again: ")

        # For each row that user wants to update...
        for column in int(columns):
            # Formatting/Keeping count.
            print(f"Column #{column} out of {columns}")

            # Prompts user to enter which column to update.
            column_name = input("Please enter name of row to update: ")

            # Prompts user to enter new data.
            data = input("Please enter updated data: ")

            # Error handling.
            try:
                # If the data is not a digit, it will be entered with quotation marks.
                if not (data.isdigit()):
                    # SQL Command.
                    cur.execute(f"UPDATE usercharacters.Characters SET {column_name} =  '{data}'")

                # If the data is not a digit, the data will not be in quotation marks 
                else: