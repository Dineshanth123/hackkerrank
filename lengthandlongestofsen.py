s=input("enter string :")
l=[]
l1=[]
x=s.split()
for i in x:
    l.append(len(i))
y=max(l)
for i in x:
    if len(i)==y:
        l1.append(i)
print(l1)    #the longest word/words in a sentence
print("the length of the longest word is :",len(l1[0]))
