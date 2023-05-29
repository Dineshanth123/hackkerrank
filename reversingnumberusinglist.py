x=int(input("enter number"))
l=[]
while(x!=0):
    y=x%10
    l.append(y)
    x=x//10
for x in l:
    print(x,end='')
