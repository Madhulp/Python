n = int(input())
a = list(map(int, input().strip().split()))[:n]
sum_of_Even = 0
sum_of_Odd = 0
for x in a:
    if x % 2 == 0:
        sum_of_Even = sum_of_Even+x
    else:
        sum_of_Odd = sum_of_Odd+x
if sum_of_Even >= sum_of_Odd:
    print("Even")
else:
    print("Odd")
