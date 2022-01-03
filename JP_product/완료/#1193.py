# 백준 1193 분수찾기
num = int(input())
i = 0
while num > 0 :
    i += 1
    num = num - i

if i % 2 == 0 :
    print(str(i+num) + "/" + str(1-num))
else:
    print(str(1-num) + "/" + str(i+num))