usestr=input()
n=""
i=0
for x in usestr:
    if usestr.index(x)==i:
        n=n+x
    i=i+1
if n==usestr:
    print('Unique')
else:   
    print('No')