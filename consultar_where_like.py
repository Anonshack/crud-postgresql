import psycopg2
from bd import connect
try:
    with connect.cursor() as cursor:
        x = "SELECT id, name, age FROM pet WHERE name like %s"
        search = "agg"
        cursor.execute(x, ("%" + search + "%",))
        pet = cursor.fetchall()

        for i in pet:
            print(i)
except psycopg2.Error as e:
    print("error: ", e)
finally:
    connect.close()
