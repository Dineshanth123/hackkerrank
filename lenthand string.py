s=input("enter string")
l=[]
l1=[]
x=s.split()
for i in x:
    l.append(len(i))
y=max(l)
for i in l:
    if y==i:
        l1.append(i)
print(l1)
z=l.index(y)
print(x[z])
print(len(x[z]))
