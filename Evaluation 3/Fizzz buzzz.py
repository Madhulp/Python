num=int(input())
num1=[]

for x in range(1,num+1):
    x=int(input())
    num1.append(x)
for x in num1:
    for n in range(1,x+1):
        if n%3==0 and n%5==0:
            print("FizzBuzz")
        elif n%5==0:
            print("Buzz")
        elif n%3==0:
            print("Fizz")
        else:
            print(n)