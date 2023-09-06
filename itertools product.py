from itertools import *
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=list(product(a,b))
for x in l:
    print(x,end=" ")
