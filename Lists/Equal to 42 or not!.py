n=int(input())
a=list(map(int,input().strip().split()))
index=0
while index<n:
    if a[index]==42:
        print("Yes")
        break
    else:
        print("No")
        break
    index+=1