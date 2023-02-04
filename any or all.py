n=int(input())
l=list(map(int,input().split()))
y=all(x>0 for x in l ) and any( x for x in l if str(x)==str(x)[::-1])
print(y)