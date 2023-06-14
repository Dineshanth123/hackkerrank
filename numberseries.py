from math import *
n=int(input("enter range"))
s=0
for x in range(1,n+1):
    s=s+(x/(factorial(x)))   #number series=1/1!+2/2!+3/3!+......+n/n!
print(s)
    
