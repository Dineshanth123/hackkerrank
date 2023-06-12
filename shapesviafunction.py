 def sphere(r):
    x=4*pi*r*r
    print("surface area of the sphre is ",x)
    y=4/3*(pi*r**3)
    print("volume of sphere is ",y)
def cylinder(r,h):
    x=(2*pi*r*r)+(2*pi*r*h)
    print("Surface area of the cylinder is ",x)
    y=pi*r*r*h
    print("volume of cylinder is ",y)
def cone(r,h,s):
    x=(pi*r*s)+(pi*r*r)
    print("surface area of cone is ",x)
    y=1/3*pi*r*r*h
    print("volume of cone is ",y)
def prism(l,w,h):
    x=2*((l*w)+l*h+(w*h))
    print("surface area of rectangular prism is ",x)
    y=l*w*h
    print("volume of rectangular prism is ",y)
def tri_prism(w,h,s,l):
    x=((w*h)+(2*l*s)+(l*w))
    print("surface area of triangular prism is ",x)
    y=1/2*(l*w*h)
    print("volume of triangular prism is ",y)
r=int(input("enter the radius "))
h=int(input("enter the height "))
w=int(input("enter the width "))
l=int(input("enter the length "))
s=int(input("enter the slant height "))
pi=3.14
sphere(r)
cylinder(r,h)
cone(r,h,s)
prism(l,w,h)
tri_prism(w,h,s,l)

