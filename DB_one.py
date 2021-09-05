import sqlite3 as db
import pandas as pd
from pandas.core.frame import DataFrame

#영양정보 DB 만들기
one = "one"
con = db.connect(one + ".db") # DB와 연결하기
wb_nu = pd.read_csv("nutrition1.csv", header=0, encoding = "CP949", dtype={"원료명칭":str, "Moisture":float, "조단백질":float, "조지방":float, "칼슘":float, "인":float, "조섬유":float, "조회분":float}) # pandas를 이용해서 CSV 파일 읽기, dtype은 column의 데이터타입 설정
wb_pr = pd.read_csv("price.csv", header=0, encoding = "CP949", dtype={"원료명":str, "업체명":str, "단가":float}, na_values=['#VALUE!']) # pandas를 이용해서 CSV 파일 읽기, dtype은 column의 데이터타입 설정, na_values는 null로 취급할 데이터들 정의

# 두 개의 DataFrame 합치기
DF1 = pd.merge(left = wb_pr, right = wb_nu, how = "outer", on = "원료명")

# DataFrame을 spl로 만들기
DF1.to_sql("one", con, index=False, if_exists="append")

'''
cur = con.cursor()
a = cur.execute("select * from one")
print(a.fetchone())
print(a.fetchone())
print(a.fetchone())
print(a.fetchone())
'''

con.close()