from math import *
x=float(input("enter x0 :"))
y=float(input("enter y0 :"))
h=float(input("enter h :"))
fun=input("enter function[NOTE:USE * FOR MULTIPLICATION,USE / FOR DIVISION] :")
n1=int(input("enter value of x :"))
n2=n1//h
n=int(n2)
print("Number of Iterations :",n)
def f(x,y):
    e=eval(fun)
    return e
for i in range(n):
    y=y+h*f(x,y)
    print("the value of y at {0} is {1}".format(round(x+h,4),round(y,4)))
    x=x+h

