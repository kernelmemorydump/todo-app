import mysql.connector

db_config = {
    "host": "127.0.0.1",
    "user": "mysql",
    "password": "mysql"
}

db_connection = mysql.connector.connect(**db_config)