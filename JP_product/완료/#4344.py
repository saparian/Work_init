# 백준 4344번 평균은넘겠지
N = int(input())
for i in range(N):
    score = list(map(int,input().split()))
    average = sum(score[1:]) / score[0]
    c = 0
    for i in score[1:]:
        if i > average:
            c += 1
    ans = c / score[0] * 100
    
    print(format(ans, ".3f") + "%")