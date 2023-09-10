l=list(map(int,input().split()))
s=input()
k=[]
for x in range(len(l)):
    for h in range(x+1,len(l)):
        if l[x]==l[h]:
            j=[x,h]
            k.append(j)
print(k)
s1=list(s)
k1=[]
for x in range(len(l)):
    for h in range(x+1,len(l)):
        if s1[x]==s1[h]:
            j1=[x,h]
            k1.append(j1)
print(k1)
res=(len(k)==len(k1)and all(x==y for x,y in zip(k,k1)) or (any(x in k1 for x in k)))
print(res)
