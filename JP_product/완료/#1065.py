# 백준 1065번 한수
'''
1. 인풋으로 받은 입력(str)을 리스트에 저장
(반복문)
2. 각 인수의 차가 동일한지 확인
2-1. 동일할 경우 새로운 리스트(Han)에 저장
2-2. 동일하지 않을 경우 넘어감
(반복문 종료)
3. Han(리스트)에 있는 갯수를 출력
'''

# 첫번째 풀이 (엄청 조잡하네)
'''
N = input()
Han = []

if int(N)<10:
    for i in range(int(N)):
        Han.append(N)
if int(N)>9:   
    for i in range(9):
        Han.append(N)
    for i in range(int(N)-9):
        I = list(str(10+i))
        gap = int(I[0]) - int(I[1])
        len_I = len(I)-1
        for i in range(len_I):
            if gap == int(I[i]) - int(I[i+1]):
                T = 0
            else :
                T = 1
        if T == 0 :
            Han.append(I)
print(len(Han))

'''


# 다른 풀이버전
a = int(input())
hansu = 0

for i in range(1, a+1):
    if i < 100 :
        hansu += 1         # 100보다 작으면 모두 한수

    else :
        Num = list(map(int, str(i)))
        if Num[0] - Num[1] == Num[1] - Num[2]: # 1000보다 작은수니까 이렇게 해도 괜찮음
            hansu += 1
print(hansu)