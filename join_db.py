import sqlite3 as db
import pandas as pd

#영양정보 DB 만들기
all = "all"
con = db.connect(all + ".db") # DB와 연결하기
wb_pr = pd.read_csv("nutrition.csv", header=0, encoding = "CP949", dtype={"원료명칭":str, "Moisture":float, "조단백질":float, "조지방":float, "칼슘":float, "인":float, "조섬유":float, "조회분":float}) # pandas를 이용해서 CSV 파일 읽기, dtype은 column의 데이터타입 설정

wb_pr.to_sql("nutrition", con, index=False, if_exists="append")  # csv 읽은 것을 sql로 변환하기


#가격 DB 만들기
wb_pr = pd.read_csv("price.csv", header=0, encoding = "CP949", dtype={"원료명":str, "업체명":str, "단가":float}, na_values=['#VALUE!']) # pandas를 이용해서 CSV 파일 읽기, dtype은 column의 데이터타입 설정, na_values는 null로 취급할 데이터들 정의

wb_pr.to_sql("price", con, index=False, if_exists="append") #CSV를 읽은 dataframe을 sql로 만들기


cur = con.cursor()
a = cur.execute("select 원료명, 단가, 업체명, Moisture, 조단백질, 조지방, 칼슘, 인, 조섬유, 조회분 from price left outer join nutrition on price.원료명 = nutrition.원료명칭")
#cur.execute("select * from nutrition")
print(a.fetchone())
print(a.fetchone())
print(a.fetchone())
con.close()
