def passcheck(str):
    print(str[::-1])
a=int(input())
b=[]
str=[]
for i in range(a):
    str.append(input())
for i in range(a):
    passcheck(str[i])