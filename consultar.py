import psycopg2
from bd import connect

try:
    with connect.cursor() as cursor:
        cursor.execute("SELECT id, name, age FROM pet;")
        temp = cursor.fetchall()
        for i in temp:
            print(i)
except psycopg2.Error as e:
    print("error: ", e)
finally:
    connect.close()
