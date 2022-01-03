# 백준 2675 문자열반복
cnt = int(input())
for i in range(cnt):
    num, chr = map(str, input().split())
    ptn = ""
    for i in list(chr):
        ptn += i*int(num)
    print(ptn)