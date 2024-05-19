import psycopg2
from bd import connect
try:
    with connect.cursor() as cursor:

        x = "SELECT id, name, age FROM pet WHERE age > %s;"
        cursor.execute(x, (1,))
        x = cursor.fetchall()

        for i in x:
            print(i)
except psycopg2.Error as e:
    print("error: ", e)
finally:
    x.close()
