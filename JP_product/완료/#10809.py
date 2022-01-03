# 백준 10809번 알파벳 찾기

'''
a = list(map(str, input()))
char = list("abcdefghijklmnopqrstuvwxyz")
Str = str()
for i in char:
    if i in a:
        Str += str(a.index(i)) + " "
    else:
        Str += str(-1) + " "
        
print(Str)
'''

# 다른 풀이
a = input()
char = list(range(97, 122)) # 아스키코드를 활용
for i in char:
    print(a.find(chr(i)), end = " ") 
    # find는 해당값을 찾아 인덱스값을 리턴해줌 (없는 경우 -1)
    # chr은 아스키코드값을 문자로 변환해줌
    # 반대로 ord는 특정 문자를 아스키코드로 변환해줌