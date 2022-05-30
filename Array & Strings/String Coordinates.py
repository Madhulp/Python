m=int(input())
s=input()
length=len(s)
if m<=length:
    x=0
    y=0
    i=0
    for i in range(i,m):
        if s[i]=='u':
            x=x+1
        elif s[i]=='d':
            x=x-1
        elif s[i]=='r':
            y=y+1
        elif s[i]=='l':
            y=y-1
    print(x,y)    