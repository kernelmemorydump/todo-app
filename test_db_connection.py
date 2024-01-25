import mysql.connector

db_config = {
    "host": "localhost",
    "user": "mysql",
    "password": "mysql"
}

db_connection = mysql.connector.connect(**db_config)