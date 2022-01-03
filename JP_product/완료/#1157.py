# 백준 1157 단어공부

word = list(input().upper())
set_word = list(set(word))
cnt = []

for i in set_word:
    cnt.append(word.count(i))
    
if cnt.count(max(cnt)) != 1:
    print("?")
else :
    print(set_word[cnt.index(max(cnt))])
