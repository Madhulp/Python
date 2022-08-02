n=int(input())
m=list(map(int,input().strip().split()))
for x in m:
    if x%2==1:
        print(x)