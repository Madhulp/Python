n=int(input())
a=list(map(int,input().strip().split()))[:n]
s=0
for x in a:
    s=s+x
avg=s/n
print(int(avg))