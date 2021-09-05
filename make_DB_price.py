import sqlite3 as db
import pandas as pd

#가격 DB 만들기
price = "price"
con = db.connect(price + ".db") # DB와 연결하기
wb_pr = pd.read_csv("price.csv", header=0, encoding = "CP949", dtype={"원료명":str, "업체명":str, "단가":float}, na_values=['#VALUE!']) # pandas를 이용해서 CSV 파일 읽기, dtype은 column의 데이터타입 설정, na_values는 null로 취급할 데이터들 정의

wb_pr.to_sql("price", con, index=False, if_exists="append") #CSV를 읽은 dataframe을 sql로 만들기



#연결된 DB에서 데이터 찾기
cur = con.cursor() #연결한 DB에 커서 만들기
cur.execute("select * from 'price' where 원료명='원료20'") # price table의 원료명 column 에 '원료20'을 가진 데이터 선택하기

rows = cur.fetchone()
print(cur.fetchone())
con.close() # 연결된 DB 끊기
