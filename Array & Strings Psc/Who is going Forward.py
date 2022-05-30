n,k=map(int,input().split(' '))
lst=list(map(int,input().split(" ")))
lst_1=lst[k-1]
count=0
for i in lst:
    if i>=lst_1 and (i>0 and lst_1>0):
        count+=1
print(count)        