import psycopg2
from bd import connect
try:
    with connect.cursor() as cursor:

        x = "DELETE FROM pet WHERE age < %s;"
        age = 2
        cursor.execute(x, (age,))
    connect.commit()
except psycopg2.Error as e:
    print("Error: ", e)
finally:
    connect.close()
