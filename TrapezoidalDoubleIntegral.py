from math import *
valid=input("enter yes for trigonometric functions or else print no :")
if valid=="yes":
    lx=int(input("enter lower limit for x in degrees :"))
    ux=int(input("enter upper limit for x in degrees :"))
    ly=int(input("enter lower limit for y in degrees :"))
    uy=int(input("enter upper limit for y in degrees :"))
    h=float(input("enter the value of h in degrees :"))
    k=float(input("enter the value of k in degrees :"))
    ran=(ux-lx)//h
    ra=int(ran)
    fun=input("enter the function :")
    def f(x,y):
        x=radians(x)
        y=radians(y)
        e=eval(fun)
        return e
    l1=[]  #stores x terms
    u=lx
    for x in range(0,ra+1):
        l1.append(u)
        u=u+h
    l2=[]  #stores y terms
    v=ly
    for x in range(0,ra+1):
        l2.append(v)
        v=v+h
    l3=[]  #contains numerics
    for x in l1:
        for y in l2:
            i=round(f(x,y),4)
            l3.append(i)
    l4=l1[1:ra]
    l41=l2[1:ra]
    l5=[]  #contains period(.) elements
    for x in l4:
        for y in l41:
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
    h=(h*pi)/180
    k=(k*pi)/180
    result=((h*k)/4)*((circle)+(2*(star))+(4*(period)))
    print("the result is :",result)
else:
    lx=int(input("enter lower limit for x :"))
    ux=int(input("enter upper limit for x :"))
    ly=int(input("enter lower limit for y :"))
    uy=int(input("enter upper limit for y :"))
    h=float(input("enter the value of h :"))
    k=float(input("enter the value of k :"))
    ran=(ux-lx)//h
    ra=int(ran)
    fun=input("enter the function :")
    def f(x,y):
        e=eval(fun)
        return e
    l1=[]  #stores x terms
    u=lx
    for x in range(0,ra+1):
        l1.append(u)
        u=u+h
    l2=[]  #stores y terms
    v=ly
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
            
            

