alph=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dig=[x for x in range(1,10000)]
l=[]
for i in alph:
    for j in alph:
        for k in dig:
            k1=str(k)
            l.append(i+j+" "+k1)
print(len(l[:1000]))   #displaying first 1000 possibilities
            
