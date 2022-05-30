n=int(input())
a=list(map(int,input().strip().split()))[:n]
a.reverse()
for x in a:
    print(x)
