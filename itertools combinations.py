from itertools import *
i=input().split()
t=i[0]
e=int(i[1])+1
s=sorted(t)
for i1 in range(1,e):
    for j in combinations(s,i1):
        print("".join(j))
