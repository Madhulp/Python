def lastDigit(num):
    return num%10
number=int(input())
last_digit=lastDigit(number)
if last_digit%3==0:
    print('Divisible')
else:
    print('Not Divisible')