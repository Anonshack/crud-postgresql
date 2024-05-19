import psycopg2
from bd import connect
try:
    with connect.cursor() as cursor:
        x = "INSERT INTO pet(name, age) VALUES (%s, %s);"
        cursor.execute(x, ("pet_pet", 1))
    connect.commit()

except psycopg2.Error as e:
    print("error: ", e)
finally:
    connect.close()
