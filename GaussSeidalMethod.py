from math import *
print("enter the values after rearranging equations")
a1=int(input("enter the value for a1 :"))
b1=int(input("enter the value for b1 :"))
c1=int(input("enter the value for c1 :"))
d1=int(input("enter the value for d1 :"))
a2=int(input("enter the value for a2 :"))
b2=int(input("enter the value for b2 :"))
c2=int(input("enter the value for c2 :"))
d2=int(input("enter the value for d2 :"))
a3=int(input("enter the value for a3 :"))
b3=int(input("enter the value for b3 :"))
c3=int(input("enter the value for c3 :"))
d3=int(input("enter the value for d3 :"))
y=0
z=0
x1=0
for i in range(1,10):
    x=(1/a1)*(d1-(b1*y)-(c1*z))
    x=round(x,4)
    if x1==x:
        break
    y=(1/b2)*(d2-(a2*x)-(c2*z))
    z=(1/c3)*(d3-(a3*x)-(b3*y))
    x1=round(x,4)
    y1=round(y,4)
    z1=round(z,4)
print("the value of x is :",x1)
print("the value of y is :",y1)
print("the value of z is :",z1)



