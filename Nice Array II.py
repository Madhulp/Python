n=int(input())
m=list(map(int,(input().strip().split())))[:n]
k=int(input())
p=[]
s=0
for x in m:
    if x%2==1:
        p.append(x)
b=len(p)
if b>k: 
    print("Nice Array")
else:
    print("Bad Array")