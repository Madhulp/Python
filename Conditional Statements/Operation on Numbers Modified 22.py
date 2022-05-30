N,M=map(int,input().split())
N=N*6
N=N+7
N=N-19
if N>M:
    print("Greater!")
elif N==M:
    print("Equal!")
else:
    print("Lesser!")
