N,X=map(int,input().split())
sum=1
if N<=0 or X<=0:
    print(-1)
else:
    i=1
    for i in range(i,N,1):
        sum=sum+X**i
    print(sum)    