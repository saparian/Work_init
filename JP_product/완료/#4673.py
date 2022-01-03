# 백준 4673번 셀프넘버
# set 함수는 중복이 없는 집합함수
''' 
1부터 시작해서 더한다
나온 수를 set에 넣는다
1~n까지 돌려가면서 set에 없는 수를 따로 관리한다

def d(a) : 
    s = set()
    for i in range(a):
        i += 1
        Str_i = str(i)
        c = 0
        for j in range(len(Str_i)):
            c += int(Str_i[j])
        i = i + c
        s.add(i)
    for i in range(a):
        i = i + 1
        if i in s:
            continue
        else :
            print(i)
    
d(10000)

'''


# 집합 두개 관리하고 빼서 출력하기

num = set(range(1,10001))
cal_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    cal_num.add(i)
s = sorted(num - cal_num)
for i in s:
    print(i)
