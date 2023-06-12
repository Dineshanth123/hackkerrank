x=list(map(int,input().split()))
s=int(input("enter element to search"))
l=len(x)
count=0
el=[]
nl=[]
for i in range(0,l):
    if(x[i]==s):
        count=count+1
        el.append(i)
        nl.append(-l+i)
print("positive indexing",el)
print(count)
print("negative indexing",nl)
        
        
