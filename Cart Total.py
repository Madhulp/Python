n=int(input())
price=list(map(int,input().strip().split()))[:n]
quantity=list(map(int,input().strip().split()))[:n]
i=0
t=0
sum=1
while i<n:
    s=price[i]*quantity[i]
    t=t+s
    i+=1
print(t)