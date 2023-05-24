s=int(input("enter your current salary"))
y=int(input("enter you year of experience"))
a=(s*10)//100
b=(s*8)//100
c=(s*5)//100
if(y>10):
    print("your bonus amount is:",a)
elif(y>6 and y<10):
    print("your bonus amount is:",b)
elif(y<6):
    print("your bonus amount is:",c)
else:
    print("invalid input")
        
