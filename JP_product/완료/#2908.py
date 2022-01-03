# 백준 2908번 상수

'''
a, b = input().split()
A = int(a[2] + a[1] + a[0])
B = int(b[2] + b[1] + b[0])

if A > B :
    print(A)
else:
    print(B)
'''

a, b = input().split()
A = int(a[::-1])
B = int(b[::-1])
if A > B:
    print(A)
else:
    print(B)    
    
