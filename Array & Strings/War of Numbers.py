n=int(input())
m=list(map(int,input().strip().split()))
odd=[]
even=[]
for x in m:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(sum(even)-sum(odd))