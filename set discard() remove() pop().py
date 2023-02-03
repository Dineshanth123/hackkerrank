n=int(input())
s=set(map(int,input().split()))
a=int(input())
for x in range(a):
    i=list(map(str,input().split(" ")))
    if i[0]=="discard":
        s.discard(int(i[1]))
    elif i[0]=="remove":
        try:
            s.remove(int(i[1]))
        except:
            pass    
    else:
        s.pop()
     
print(sum(s))