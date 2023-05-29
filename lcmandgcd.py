l=[]
l1=[]
l2=[]
x=int(input("enter value for a:"))
y=int(input("enter value for b:"))
for i in range(1,11):
    l.append(x*i)
for i in range(1,11):
    l1.append(y*i)
for s in l:
    for t in l1:
        if(s==t):
            l2.append(s)
lcm=l2[0]
print("lcm of {x} and {y} is {z}".format(x=x,y=y,z=lcm))
gcd=(x*y)//lcm
print("gcd of {x} and {y} is {z}".format(x=x,y=y,z=gcd))
