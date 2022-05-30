N=int(input())
M=list(map(int,input().split()))
str1=[]
if (N>1):
    for i in range(N-1):
        if (M[i] in M[i+1:]):
            str1.append(M[i])
        else:
            pass
    if (len(str1))==0:
        print(M[0])
    else:
        if (len(str1)>1):
            while(len(str1)>2):
                str2=[]
                count=0
                for i in range(len(str1)-1):
                    if (str1[i]) in str1[i+1:]:
                        str2.append(str1[i])
                    else:
                        count+=1
                if (count==len(str1)):
                    break
                else:
                    str1=str2
            print(str1[0])
        else:
            print(str1[0])
else:
    print(M[0])
    
                    