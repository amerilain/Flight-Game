import mysql.connector
import mariadb

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='arina',
    password='1234',
    autocommit=True
)

def game_goals (id):
    description = "SELECT id, name, description FROM goal"
    description += " WHERE id='" + id + "'"
    print(description)
    cursor = connection.cursor()
    cursor.execute(description)
    result = cursor.fetchall()
    while cursor.rowcount <= 8:
        for row in result:
            print(f"The goal number {row[1]} is to fly to a country where the weather is {row[2]} and {row[3]}.")
    return








