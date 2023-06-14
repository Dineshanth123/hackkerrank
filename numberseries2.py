x=int(input("enter number of interest"))
n=int(input("enter number range"))
i=1
s=0
t=2
while(i<=n):       #number series=x/2+x/4+x/8+.....+n
    s=s+x/t
    t=t*2
    i=i+1
print(s)
    
    
