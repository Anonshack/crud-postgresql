import psycopg2
from bd import connect

try:
    with connect.cursor() as cursor:
        cursor.execute("SELECT id, name, age FROM pet;")
        x = cursor.fetchone()
        while x:
            print(x)
            x = cursor.fetchone()
except psycopg2.Error as e:
    print("error: ", e)
finally:
    connect.close()
