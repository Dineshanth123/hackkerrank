x=list(map(float,input().split()))
y=list(map(float,input().split()))
t1=y
h=x[1]-x[0]
x0=x[-1]
t=int(input("enter the value of x to calculate"))
u=(t-x0)/h
lx=len(x)
la=lx
ly=len(y)
l1=[]
l2=[]
i=1
p=0
lx1=lx-1
la1=la-1
for k in range(lx1):
    for j in range(0,la1):
        l1.append(y[i]-y[j])
        i=i+1
    l2.append(list(l1))
    l1.clear()
    y=l2[p]
    p=p+1
    i=1
    la1=la1-1
l3=[]
for r in range(lx1):
    l3.append(l2[r][-1])
print(l3)
def fac(n):
    if n<=1:
        return 1
    else:
        return n*fac(n-1)
def fact(u,r):
    if r==1:
        return u
    else:
        fact=u
        for x in range(1,r):
            fact=fact*(u+x)
        return fact

res=t1[-1]
for c in range(1,lx1):
    res=res+(((l3[c-1])/(fac(c)))*(fact(u,c)))
print("the result is: ",round(res,4))
    
