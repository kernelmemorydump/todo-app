import mysql.connector

db_config = {
    "host": "localhost",
    "user": "mysql",
    "password": "mysql",
    "database": "todo", # Ovo dodajemo pri kreiranju table-a jer prvi put ne selektujemo bazu, kada je pravimo
}

db_connection = mysql.connector.connect(**db_config)
db_cursor = db_connection.cursor()

"""Prvi put samo kreiramo databazu"""
#db_cursor.execute("CREATE DATABASE todo")

"""Drugi put kreiramo table"""
db_cursor.execute("CREATE TABLE `todo_tasks` (`id` INT NOT NULL AUTO_INCREMENT, `ime` VARCHAR(255), `zavrseno` BOOLEAN, PRIMARY KEY (`id`));")