dire=input()
my_list=len(dire)
a=0
b=0
for x in range(my_list):
    if dire[x]=='L':
        a=a-1
    elif dire[x]=='R':
        a=a+1
    elif dire[x]=='D':
        b=b-1
    elif dire[x]=='U':
        b=b+1
    else:
        a=a
        b=b
print(a,b)   