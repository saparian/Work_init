#백준 8958 OX퀴즈
'''
N = int(input())
for j in range(N):
    Q = input()
    num = [0]
    for i in range(len(Q)):
        if Q[i] == "O":
            num.append(num[i]+1)
        else:
            num.append(0)
    print(sum(num))
'''

N = int(input())
for i in range(N):
    Str = input()
    Q = list(Str)
    Sum = 0
    count = 1
    for j in Q:
        if j == "O":
            Sum += count
            count += 1
        else:
            count = 1
    print(Sum)