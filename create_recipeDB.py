import sqlite3 as db
import pandas as pd
import datetime

'''임시데이터
a = "업체1"
b = "제품1"
c = [['원료1', 1], ['원료2', 2]]
c = "'" + str(c) + "'"
#print(c)
#print(c.strip("'"))
d = []
d.append(a)
d.append(b)
d.append(c)
e = datetime.datetime.now()
f = e.strftime('%Y-%m-%d')
#print(f)
d.append(f)'''

recipe = "recipe"
con = db.connect(recipe + ".db")
cur = con.cursor()
cur.execute('create table if not exists recipe (name_company, product_name, material, date)')
#cur.execute('insert into recipe values (?,?,?,?)', d)
a = cur.execute('select * from recipe')


print(a.fetchall())
con.commit()

con.close()