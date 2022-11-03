import mysql.connector
import redis
from secrets import choice
from time import time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "testpw",
    database = "mydatabase"
)

sql_cursor = mydb.cursor()


sql_cursor.execute("SELECT * FROM customers")

key_list = [x[0] for x in sql_cursor.fetchall()]

random_key_list = []

for _ in range(20000):
    random_key_list.append(choice(key_list))

start_time = time()

for key in random_key_list:
    sql_cursor.execute(f"SELECT address FROM customers WHERE name ='{key}' ")
    myresult = sql_cursor.fetchall()
    
end_time = time()

timeDel = end_time - start_time
print(timeDel)

r = redis.Redis()

start_time = time()
for key in random_key_list:

    myresult = r.get(key)

end_time = time()

timeDel = end_time - start_time
print(timeDel)