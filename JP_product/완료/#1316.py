# 백준 1316번 그룹단어 체커
'''
실패한 코드
num = int(input())
group_word = 0
for i in range(num):
    word = input()
    c = 0
    for i in word:
        if i == word[word.find(i) + word.count(i) -1]:
            continue
        else : 
            c = -1
            break
    if c == 0 : 
        group_word += 1
print(group_word)

반례 : abbbaaaaa, abaa
'''

'''
#풀이
num = int(input())
cnt = 0
for i in range(num):
    word = input()
    c = 0
    for j in word:
        k = word.count(j)
        for l in range(k):
            if word[l+word.index(j)] == j:
                continue
            else:
                c = -1
                break
    if c == 0:
        cnt += 1
    
print(cnt)
'''
num = int(input())
cnt = 0
for i in range(num):
    word = input()
    error = 0
    for j in range(len(word)-1):   # 글자 1개짜리는 이미 그룹단어이므로 반복문으로 검증할 필요가 없음
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if new_word.count(word[j]) > 0:
                error += 1
    if error == 0 :
        cnt += 1
print(cnt)

