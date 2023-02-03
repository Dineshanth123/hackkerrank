from collections import Counter
k=int(input())
l=list(map(int,input().split()))
l=Counter(l).items()
keys=[k for k,v in l if v==1 ]
for x in keys:
    print(x)