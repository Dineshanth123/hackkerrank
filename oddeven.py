x=int(input("enter number range"))
o=[x for x in range(0,x+1)if x%2!=0]
e=[x for x in range(0,x+1)if x%2==0]
print("odd counts=",len(o))
print("even counts=",len(e))

