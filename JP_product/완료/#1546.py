#백준 1546 평균
# input 1 =과목수 = N
# input 2 = 현재 성적

N = int(input())
score = []
score = list(map(int, input().split()))
#print(score)
Max = max(score)
#print(Max)
sc = []
for i in score:
    sc.append(i/Max*100)

Sum = sum(sc)
print(Sum/N)
