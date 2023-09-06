from itertools import permutations
i=input().split()
s=i[0]
intt=int(i[1])
li1=list(permutations(s,intt))
li=sorted(li1)
for x in li:
    for y in x:
        print(y,end="")
    print(sep=" ")

