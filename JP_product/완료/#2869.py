# 백준 2869 달팽이는 올라가고 싶다.
import math
A, B, V = map(int, input().split())
V = V-A
print(math.ceil(V / (A-B))+1)
