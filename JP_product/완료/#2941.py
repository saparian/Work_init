# 백준 2941번 크로아티아 알파벳
'''    
alphabet_1 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet_2 = ['dz=']

word = input()
c=0
for i in alphabet_1:
    c += word.count(i)

for i in alphabet_2:
    c += word.count(i)
    
print(len(word)-c)
'''
    
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in cro:
    word = word.replace(i, '*')
print(len(word))