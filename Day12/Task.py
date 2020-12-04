import sqlite3
import json

conn = sqlite3.connect("task.db")
print("Creating the database")

cursor = conn.cursor()
try:
    cursor.execute("CREATE TABLE OF MINE"
                   "("
                   + "dictinary BLOB,"
                   + "list BLOB,"
                   + "tuple BLOB,"
                   + "string varchar(50),"
                   + "Integer INTEGER,"
                   + "flo FLOAT,"
                   + "Bool BOOLEAN,"
                   + "None BLOB"
                     ");")
except Exception as e:
    print("Error :", e)
else:
    print("Table created")

datafile = open("task.json")
dataset = json.load(datafile)
dataframe = []
for row in dataset:
    data = (str(row[0]), str(row[1]), str(row[2]), str(row[3]), int(row[4]),float(row[5]), bool(row[6]), row[7])
    dataframe.append(data)

try:
    cursor.executemany("INSERT INTO MINE VALUES (?,?,?,?,?,?,?,?)", dataframe)
except Exception as e:
    print("Error : ", e)
else:
    conn.commit()
    print("Data inserted")


try:
    cursor.execute("SELECT * from MINE")
except Exception as e:
    print("Error : ", e)
else:
    for row in cursor.fetchall():
        print(row)

conn.close()