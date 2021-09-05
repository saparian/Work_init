
import numpy as np
import pandas as pd
import sqlite3 as db

data = []

while True:
    stuff = input("원료명 : ")
    # 엔터키 입력시 반복문 종료
    if stuff == "":
        break;
    add = input("투입량 : ")
    try:
        add = float(add)
    except ValueError:
        add = input("에러 : 수치를 입력해주세요 \n 투입량 :  ")
        add = float(add)
    # 원료 및 투입량 리스트에 저장
    data.append([stuff, add]) 


# data를 dataframe 만들어서 표현하기
table = pd.DataFrame(data, columns=['원료명','kg'])

# 'kg' 컬럼의 합계 구하기
sum_kg = table['kg'].sum()

# '함량' column 추가하기
table['함량(%)'] = table['kg']* 100 / sum_kg

# '원료명' column을 리스트로 변환
t1 = np.array(table['원료명'])

# DB 연결하기
con = db.connect("one.db")

#커서 만들기
cur = con.cursor()

# DB에서 원하는 column의 data 추출해서 리스트로 만들기
price = []
i = 0
for s in t1: # for문에서 변수 s는 str이 됨
    s = t1[i]  # t1은 ()가 아닌 []를 사용해야함
    cur.execute(f"select 단가 from one where one.원료명 == '{s}'")
    s1 = cur.fetchone()
    s2 = int(s1[0])
    price.append(s2)
    i = i + 1
con.close()

# 단가 리스트를 table에 추가
table["원료단가"] = price

# 원료 단가를 기반으로 실제 반영되는 단가를 table에 추가
table["실제단가"] = table["함량(%)"] * table["원료단가"] / 100

# 'kg' 컬럼의 합계 구하기
sum_pr = table['실제단가'].sum()




# DB 재연결하기
con = db.connect("one.db")

#커서 만들기
cur = con.cursor()

# DB에서 원하는 column의 data 추출해서 리스트로 만들기
Moisture = []
Cp = []
Cf = []
Ca = []
p = []
fiber = []
Ash = []

i = 0
for s in t1: # for문에서 변수 s는 str이 됨
    s = t1[i]  # t1은 ()가 아닌 []를 사용해야함
    cur.execute(f"select ifnull(Moisture, 0), ifnull(조단백질,0), ifnull(조지방,0), ifnull(칼슘,0), ifnull(인,0), ifnull(조섬유,0), ifnull(조회분,0) from one where one.원료명 == '{s}'")
    s1 = cur.fetchone()
    # Moisture 리스트 만들기
    s2 = float(s1[0])
    Moisture.append(s2)
    # Cp 리스트 만들기
    s3 = float(s1[1])
    Cp.append(s3)
    # Cf 리스트 만들기
    s4 = float(s1[2])
    Cf.append(s4)
    # Ca 리스트 만들기
    s5 = float(s1[3])
    Ca.append(s5)
    # p 리스트 만들기
    s6 = float(s1[4])
    p.append(s6)
    # fiber 리스트 만들기
    s7 = float(s1[5])
    fiber.append(s7)
    # Ash 리스트 만들기
    s8 = float(s1[6])
    Ash.append(s8)
    i = i + 1
con.close()

# Moisture 리스트를 table에 추가
table["수분"] = Moisture * table["함량(%)"]

# Cp 리스트를 table에 추가
table["조단백질"] = Cp * table["함량(%)"]

# Cf 리스트를 table에 추가
table["조지방"] = Cf * table["함량(%)"]

# Ca 리스트를 table에 추가
table["칼슘"] = Ca * table["함량(%)"]

# p 리스트를 table에 추가
table["인"] = p * table["함량(%)"]

# fiber 리스트를 table에 추가
table["조섬유"] = fiber * table["함량(%)"]

# Ash 리스트를 table에 추가
table["조회분"] = Ash * table["함량(%)"]


# '수분' 컬럼의 합계 구하기
sum_Moisture = table['수분'].sum()

# 'Cp' 컬럼의 합계 구하기
sum_Cp = table['조단백질'].sum()
# 'Cf' 컬럼의 합계 구하기
sum_Cf = table['조지방'].sum()
# 'Ca' 컬럼의 합계 구하기
sum_Ca = table['칼슘'].sum()
# 'p' 컬럼의 합계 구하기
sum_p = table['인'].sum()
# 'fiber' 컬럼의 합계 구하기
sum_fiber = table['조섬유'].sum()
# 'Ash' 컬럼의 합계 구하기
sum_Ash = table["조회분"].sum()

#일반성분 리스트
content = [sum_Moisture, sum_Cp, sum_Cf, sum_Ca, sum_p, sum_fiber, sum_Ash]

print("배합표가 완성되었습니다.")
print(table)

print("총 중량 : " + str(sum_kg) + "kg")
print("원재료비 : "+ str(sum_pr) + "원/kg")
print(content)
