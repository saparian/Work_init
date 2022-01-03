# 백준 5622번 파이썬

word = input()
board = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sec = 0
for i in range(len(word)):
    for j in board:
        if word[i] in j:
            sec += board.index(j) + 3
print(sec)
        