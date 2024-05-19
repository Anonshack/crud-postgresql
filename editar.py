import psycopg2
from bd import connect
try:
    with connect.cursor() as cursor:
        x = "UPDATE pet SET age = %s WHERE id = %s;"
        new_age = 5
        new_id = 17
        cursor.execute(x, (new_age, new_id))
    connect.commit()
except psycopg2.Error as e:
    print("error: ", e)
finally:
    connect.close()
