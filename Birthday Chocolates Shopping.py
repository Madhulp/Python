rupees=int(input())
no_of_student=int(input())
if rupees>=5*no_of_student:
    print("Dairy Milk")
elif rupees>=2*no_of_student:
    print("Shots")
elif rupees==no_of_student:
    print("Eclairs")
else:
    print("No Chocolates")
