import sqlite3 as db
import pandas as pd
import datetime

a = "업체1"
b = "제품1"
c = [['원료1', 1], ['원료2', 2]]
c = "'" + str(c) + "'"
print(c)
print(c.strip("'"))
d = []
d.append(a)
d.append(b)
d.append(c)
e = datetime.datetime.now()
f = e.strftime('%Y-%m-%d')
print(f)
d.append(f)
print(d)


