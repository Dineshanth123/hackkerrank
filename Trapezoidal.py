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
add=0
for p in range(1,a):
    add=add+l[p]
y=round(add,4)
res=(h/2)*(x+(2*(y)))
print("the result is :",res)
   
