n=int(input())
a=list(map(int,input().strip().split()))
total=0
index=1
while index<n:
    total=total+a[index]
    index+=2
print(total)  