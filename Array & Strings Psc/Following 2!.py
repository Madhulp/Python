usestr=int(input())
n=list(map(int,input().split()))
for x in range(0,usestr):
    if x==0 and n[x]==2:
        print(-1)
    elif x==4 and n[x]==2:
        print(-1)
    elif n[x]==2:
        t=x+1
        print(n[t])
        