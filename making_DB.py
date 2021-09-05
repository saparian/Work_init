import sqlite3 as db
import pandas as pd

#가격 DB 만들기
price = "price"
con = db.connect(price + ".db")
wb_pr = pd.read_csv("price.csv", encoding = "euc-kr")

for sheet in wb_pr:
    wb_pr[sheet].to_sql(sheet, con, index = False, if_exists='append')
    con.commit()
con.close()

#원료 성분 DB 만들기
nutrition = "nutrition"
con = db.connect(nutrition + ".db")
wb_nu = pd.read_csv("nutrition.csv", encoding = "euc-kr")

for sheet in wb_nu:
    wb_nu[sheet].to_sql(sheet, con, index = False, if_exists='append')
    con.commit()
con.close()

####################
####################
'''
def viewDBdata(db, table):
    #SQLite DB 연결
    conn = splite3.connect(db)

    #Connection 으로부터 Cursor 생성
    cur = conn.cursor()

    #SQL 쿼리 실행
    query = "select * from {0}".format(table)
    cur.execute(query)

    #데이터 Fetch
    rows = cur.fetchall() #모든 데이터를 한번에 클라이언트로 가져옴
    for row in rows:
        print(row)

    #Connection 닫기
    cur.close()

viewDBdata("price.db", price)
'''
