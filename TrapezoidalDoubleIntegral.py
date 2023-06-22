from math import *
l=int(input("enter lower limit :"))
u=int(input("enter upper limit :"))
h=float(input("enter the value of h :"))
k=float(input("enter the value of k :"))
ran=(u-l)//h
ra=int(ran)
fun=input("enter the function :")
def f(x,y):
    e=eval(fun)
    return e
l1=[]  #stores x terms
u=l
for x in range(0,ra+1):
    l1.append(u)
    u=u+h
l2=[]  #stores y terms
v=l
for x in range(0,ra+1):
    l2.append(v)
    v=v+h
l3=[]  #contains numerics
for x in l1:
    for y in l2:
        i=round(f(x,y),4)
        l3.append(i)
l4=l1[1:ra]
l5=[]  #contains period(.) elements
for x in l4:
    for y in l4:
        q=round(f(x,y),4)
        l5.append(q)
period=sum(l5)
cir=list(map(float,(l3[0],l3[-1],l3[ra],l3[(ra+1)*ra])))  #contains circle elements
circle=sum(cir)
l6=l5+cir  #contains period and circle elements
l7=[]    #contains star elements
for x in l3:
    if x not in l6:
        l7.append(x)
star=sum(l7)
print("the period elements :",l5)
print("the star elements :",l7)
print("the circle elements :",cir)
result=((h*k)/4)*((circle)+(2*(star))+(4*(period)))
print("the result is :",result)

    
