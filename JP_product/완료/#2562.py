# 백준 2562번
num = []
cal = []
dit = {}
for i in range(10):
    num.append(int(input()))
    cal.append(num[i]%42)
for i in cal:
    try :
        dit[i] = + 1
    except :
        dit[i] = 1
print(num)
print(cal)
print(dit)
a=list(dit.keys())
print(len(a))