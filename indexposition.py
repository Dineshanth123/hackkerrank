l=[1,2,1,1,5]
k=[]
for x in range(len(l)):
    for h in range(x+1,len(l)):
        if l[x]==l[h]:
            k.append(h)
            k.append(x)
print(set(k))
        
