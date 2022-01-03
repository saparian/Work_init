# 백준 10250 ACM호텔
'''
import math
num = int(input())
for i in range(num):
    h, w, n = map(int, input().split())
    order = math.ceil(n / h)
    floor = n % h
    if floor == 0 : 
        floor = h
    else:
        floor = n % h
    if order < 10 :
        print("{0}0{1}".format(floor, order))
    else:
        print("{0}{1}".format(floor, order))
'''

num = int(input())

for i in range(num):
    h, w, n = map(int, input().split())
    floor = n % h
    order = n // h + 1
    if n % h == 0:
        floor = h
        order = n // h
    print(floor * 100 + order)