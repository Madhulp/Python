n=int(input())
l=[]
for x in range(1,n+1):
    l.append(x)
    
for x in l:
    if x%2==1:
        print(n*'_',end='\n')
    else:
        print(n*'*',end='')
        print()