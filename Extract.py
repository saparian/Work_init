import sqlite3
'''
def viewDBdata(db, table):
    #SQLite DB 연결
    conn = splite3.connect(db)

    #Connection 으로부터 Cursor 생성
    cur = conn.cursor()

    #SQL 쿼리 실행
    query = "select * from {0}".format(table)
    cur.execute(query)


viewDBdata('price.db', wb_pr)
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
'''


conn = sqlite3.connect("nutrition.db")
cur = conn.cursor()
c = conn.cursor()
cur.execute("select * from sqlite_master")

rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()
