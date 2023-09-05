import re
n=int(input())
s=set(map(int,input().split()))
l=int(input())
a='intersection_update'
b='update'
c='symmetric_difference_update'
d='difference_update'   
for x in range(l):
    s1=input()
    s3=s1.split()
    s2=s3[0]
    if s2==a:
        s3=set(s2)
        x=set(map(int,input().split()))
        s.intersection_update(x)
    elif s2==b:
        s3=set(s2)
        x=set(map(int,input().split()))
        s.update(x)
    elif s2==c:
        s3=set(s2)
        x=set(map(int,input().split()))
        s.symmetric_difference_update(x)
    else :
        s3=set(s2)
        x=set(map(int,input().split()))
        s.difference_update(x)
print(sum(s))
        
        
        
             




    
    
