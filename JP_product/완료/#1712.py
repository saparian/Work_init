# 백준 1712 손익분기점
'''
# 반복문 사용시 시간 초과로 실패하게 됨 
a, b, c = map(int, input().split())
i = 0
if b < c:
    while True:
        i += 1
        cost = a + (b * i)
        income = c * i
        if income / cost > 1:
            print(i)
            break
if b >= c :
    print(-1)
'''
a, b, c = map(int, input().split())
i = 0
if b < c:
    print(a//(c-b) + 1)

if b >= c :
    print(-1)

