import psycopg2
import json

try:
    with open("pet.json") as x:
        file_contents = x.read()
        if not file_contents:
            print("File is empty")
        else:
            temp = json.loads(file_contents)
            connect = psycopg2.connect(**temp)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
except psycopg2.Error as e:
    print("PostgresSQL:", e)
