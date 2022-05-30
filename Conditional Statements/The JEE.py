Physics1,Chemistry1,Mathematics1=map(int,input().split())
Physics2,Chemistry2,Mathematics2=map(int,input().split())

Student1=Physics1+Chemistry1+Mathematics1
Student2=Physics2+Chemistry2+Mathematics2
if Student1==Student2:
    if Mathematics1==Mathematics2:
        if Physics1>Physics2:
            print("First")
        else:
            print("Second")
    elif Mathematics1>Mathematics2:
        print("First")
    else:
        print("Second")
elif Student1>Student2:
    print("First")
else:
    print("Second")
