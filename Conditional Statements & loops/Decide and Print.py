N = int(input())
for x in range(1, N+1):
    if x % 3 == 0 and x % 5 == 0:
        print("MasaiSchool")
    elif x % 3 == 0:
        print("Masai")
    elif x % 5 == 0:
        print("School")
    else:
        print(x)
