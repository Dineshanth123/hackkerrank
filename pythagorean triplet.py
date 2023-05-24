n1=int(input("enter first number pythagorean triplet"))
n2=int(input("enter second number pythagorean triplet"))
n3=int(input("enter third number pythagorean triplet"))
if(n1<n2<n3):
    g=(n1*n1)+(n2*n2)
    h=n3*n3
    if(g==h):
        print("1")
    else:
        print("0")
else:
    print("invalid input")
