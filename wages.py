x=input("enter the name")
y=int(input("enter your age"))
g=input("enter youer gender")
d=int(input("enter number of days worked"))
if((y>=18 and y<30) and g=='m'):
    print("your wage is:",d*700)
elif((y>=18 and y<30) and g=='f'):
    print("your wage is:",d*750)
elif((y>=30 and y<=40) and g=='m'):
    print("your wage is:",d*800)
elif((y>=30 and y<=40) and g=='f'):
    print("your wage is:",d*800)
else:
    print("invalid input")
