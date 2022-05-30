num=int(input())
flag=0
num_temp=num
while num_temp>0:
    temp=num_temp%10
    num_temp//=10
    if temp!=4 and temp!=7:
        flag=1
        break
    
    
if flag==0:
    print("YES")
elif num%4==0 or num%7==0:
    print("YES")
else:
    print("NO")