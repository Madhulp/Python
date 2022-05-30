N,M=map(int,input().split(' '))
diff_level=list(map(int,input().split()))[:N]
marks=0
skip=0
for i in range(N):
    if diff_level[i]>M:
        skip+=1
        if skip>1:
            break
    else:
        marks+=1
print(marks)        