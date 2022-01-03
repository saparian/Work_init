# 백준 2292 벌집
'''
# 수학공식을 이용한 풀이
num = int(input())
i = 0
while True :
    i += 1
    if num <= 3*i*(i-1)+1 : 
        print(i)
        break
'''

num = int(input())
i = 0
cnt = 1
while True:
    cnt = cnt + 6 * i
    if num <= cnt :
        print(i+1)
        break
    i += 1