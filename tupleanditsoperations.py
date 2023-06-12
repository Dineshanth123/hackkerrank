t=tuple(input().split())
print(t)
print(''.join(t))
a=len(t)-1
l=[]
for i in range(a,-1,-1):
    l.append(t[i])
print("reversed tuple",tuple(l))
    

