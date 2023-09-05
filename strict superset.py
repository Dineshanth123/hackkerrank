l=list(map(int,input().split()))
set1=set(l)
n=int(input())
l1=[]
for x in range(n):
    l=list(map(int,input().split()))
    set2=set(l)
    leng=len(set2)
    if(set2.issubset(set1)and(len(set1)!=leng)):
        l1.append(1)
    else:
        l1.append(0)
if 0 in l1:
    print('False')
else:
    print("True")
