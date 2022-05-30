max,min=map(int,input().split())
sum_even=0
for number in range(min,max):
    if number%2==0:
        sum_even+=number
print(sum_even)