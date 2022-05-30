left,right,k=map(int,input().split())
count=0
for i in range(left,right+1):
    if i%k==0:
        count=count+1
print(count)