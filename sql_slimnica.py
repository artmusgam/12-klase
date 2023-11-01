import mysql.connector

db = mysql.connector.connect(host= "localhost", database = "slimnica", user = "root", password = "admin")
print(db)

cursor = db.cursor()

sql = ("""
insert into dakteris (idDakteris, dakteris_vards, dakteris_uzvards, dakteris_Tel)
values (%s,%s,%s,%s);
        """)

data = (1,"Artjoms","Tutins","23456789")
cursor.execute(sql,data)
db.commit()
db.close()