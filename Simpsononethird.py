from math import *
l=int(input("enter the lower limit :"))
u=int(input("enter the upper limit :"))
n=int(input("enter number of terms :"))
fun=input("enter function :")
h=(u-l)//n
print("the value of h is :",h)
l=[]
def f(x):
    t=eval(fun)
    return round(t,4)
for i in range(u+1):
    s=f(i)
    l.append(s)
x=l[0]+l[-1]
a=len(l)-1
l1=[]
for p in range(1,a):
    if p%2==0:
        continue
    l1.append(l[p])
add=sum(l1)
y=round(add,4)
l2=[]
for p in range(1,a):
    if p%2!=0:
        continue
    l2.append(l[p])
add1=sum(l2)
y=round(add1,4)
res=(h/3)*(x+(4*(add))+(2*(add1)))
print("the result is :",res)
   
