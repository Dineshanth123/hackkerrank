x=int(input("enter your number"))
l=[]
for i in range(1,x+1):
    if((i*(x//i))==x):
        l.append(i)
if(sum(l)==1+x):
    print("entered number is prime number")
else:
    print("entered number is composite/not a prime number")
