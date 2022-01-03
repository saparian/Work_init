# 백준 11654 아스키코드
# 내가 푼 방법
'''
a = input()
ascii = list("0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[/]^_`abcdefghijklmnopqrstuvwxyz")
print(48 + ascii.index(a))
'''
# 풀이방법

a = input()
print(ord(a)) # ord 함수는 아스키코드값을 리턴하는 함수