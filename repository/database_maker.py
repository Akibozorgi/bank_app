import mysql.connector

def create_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root141216"
    )
    cursor = connection.cursor()

    with open("repository/database.sql") as f:
        for sql_command in f.read().split("--"):
            try:
                print(sql_command)
                cursor.execute(sql_command)
                connection.commit()
            except Exception as e:
                print("Error :",e)
