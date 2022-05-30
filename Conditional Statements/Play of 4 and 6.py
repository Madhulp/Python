n=int(input())
if n%4==0 and n%6==0:
    print("Awesome!")
elif n%4==0:
    print("Four!")
elif n%6==0:
    print("Six!")
else:
    print("Dark!")