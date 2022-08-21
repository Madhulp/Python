def passchecker(m, str):
    character = 0
    digits = 0
    list1 = list(str)
    for i in range(m):
        if list1[i].isalpha():
            character += 1
        else:
            digits += 1
    if digits > 0 and character > (m//2):
        print('Strong')
    else:
        print('Weak')


a = int(input())
m = []
str = []
for i in range(a):
    m.append(int(input()))
    str.append(input()[:m[i]])
for i in range(a):
    passchecker(m[i], str[i])
