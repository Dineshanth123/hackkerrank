x=[10,20,15]
count1=len(x)-1
x1=0
res=0
l=[]
for y in range(count1):
    acc=x[y]
    res=res+acc
    l.append(res)
print(l)
sum1=sum(l)
count2=len(l)
avg1=sum1/count2
print(avg1)
    
    
