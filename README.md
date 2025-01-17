# Anime Character Database ⭐️
A python project that allows the user to connect to a Postgres SQL Server and gives users the option to:
- Add a character to the database
- View all records in the database.
- Select a certain record.
- Update a specified record.
- Delete a specified record.

# How do you run this program? ⭐️⭐️
> [!IMPORTANT]  
> For these steps to go smoothly, you will need install both Python and Git.
- Clone repository and run it in your python interpreter by running `git clone https://github.com/e4fgg/Anime-Character-Database`
- Install the required libraries from requirements.txt by running
`pip install -r requirements.txt` in your command-line.
- To run this program, you're going to have to download an sql server.

# How do you log into an SQL Server from Python? ⭐️⭐️⭐️
> [!IMPORTANT]  
> Make sure you have an SQL Server installed, if you don't, look below at the Resources section and download one from there.
- Sample Code: 
```python
# Import library.
import psycopg2

# Connect SQL server to Python.
connect = psycopg2.connect(
    database = "dbname",
    user = "your_server_user",
    password = "your_server_password",
    host = "your_servers_host"
)
```
# Resources ⭐️⭐️⭐️⭐️
> [!NOTE]  
> I have provided both a paid and free option that allows you to select and query data from a Postgres SQL Server, take into consideration your operating system, for reference, I use MacOS and DBeaver suffices.
- Download Python: https://www.python.org/downloads/
- Download Git: https://git-scm.com/downloads
- IDE With Python Interpreter: https://code.visualstudio.com
- Postgres SQL Server Download Link: https://www.postgresql.org/download/
- DataGrip (Paid) - https://www.jetbrains.com/datagrip/
- DBeaver Community (Free) - https://dbeaver.io



