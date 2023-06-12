s1=input("enter string1")
s2=input("enter string2")
count=0
j=0
for i in range(0,len(s1)):
     if(s1[i]==s2[j]):
            count=count+1
            j=j+1
if(count==len(s2)):
    print("yes")
else:
    print("no")
            
