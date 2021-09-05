import sqlite3 as db
import pandas as pd
import datetime

a = input("조회 / 추가 : ")

# (업체명, 제품명, 레시피[], 수정일)
if a == "조회":
    x = '업체1'
    #y = input()
    con = db.connect('recipe.db')
    cur = con.cursor()
    b = cur.execute(f'select material from recipe where name_company == "{x}"')
    #where 'x' = name_company and 'y' = product_name
    b1 = b.fetchone()
    b2 = b1[0]
    b2 = str(b2)
    print(type(b2))
    b2 = b2.strip("'")
     
    b3 = []
    print(b2)
    b3.append[b2]
    print(b3)

