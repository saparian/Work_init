import sqlite3 as db
import pandas as pd

#영양정보 DB 만들기
nutrition = "nutrition"
con = db.connect(nutrition + ".db") # DB와 연결하기
wb_pr = pd.read_csv("nutrition.csv", header=0, encoding = "CP949", dtype={"원료명칭":str, "Moisture":float, "조단백질":float, "조지방":float, "칼슘":float, "인":float, "조섬유":float, "조회분":float}) # pandas를 이용해서 CSV 파일 읽기, dtype은 column의 데이터타입 설정

wb_pr.to_sql("nutrition", con, index=False, if_exists="append")  # csv 읽은 것을 sql로 변환하기



#연결된 DB에서 데이터 찾기
cur = con.cursor() #연결한 DB에 커서 만들기
cur.execute("select * from 'nutrition' where 원료명칭='원료5'") # nutrition table의 원료명칭 column 에 '원료5'을 가진 데이터 선택하기

rows = cur.fetchone()
print(cur.fetchone())
con.close() # DB 연결 끊기
