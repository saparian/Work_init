import os

print(os.getcwd())
f = open('JP_product/a.txt', mode='rt', encoding="utf-8")
print(f)
print(f.readline())
print(f.readline())
print(f.readline())