for i in range(int(input())):
    m=int(input())
    p=list(map(int,input().split()))
    n=0
    for j in range(m):
        if p[j]%2==0:
            n=n+1
            if n==3:
                break
        else:
            n=0
    if n==3:
        print('Yes')
    else:
        print('No')
