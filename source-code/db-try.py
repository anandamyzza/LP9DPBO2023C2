import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_ormawa"
)

# INSERT
dbcursor = mydb.cursor()

sql = "INSERT INTO divisi (divisi_id, divisi_nama) VALUES (%s, %s)"
val = ("", "Divisi Gaming")
dbcursor.execute(sql, val)

mydb.commit()

print(dbcursor.rowcount, "record inserted.")

# SELECT
dbcursor = mydb.cursor()

dbcursor.execute("SELECT * FROM jabatan")

myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

# DELETE
dbcursor = mydb.cursor()

dbcursor.execute("DELETE FROM divisi WHERE divisi_nama = 'Divisi Gaming'")

mydb.commit()

print(dbcursor.rowcount, "record(s) deleted")