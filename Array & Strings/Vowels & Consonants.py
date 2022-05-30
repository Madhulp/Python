n=int(input())
i=0
while(i<n):
    A=int(input())
    B=input()
    C=int(input())
    D=input()
    P=''
    Q=''
    for x in B:
        if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
            P=P+x
    for y in D:
        if (y!='a' and y!='e' and y!='i' and y!='o' and y!='u'):
            Q=Q+y
    print(P+Q)
    i+=1
   