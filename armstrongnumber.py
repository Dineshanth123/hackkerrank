for a in range(1,501):
    z=str(a)
    y=sum([int(s)**3 for s in z])
    if(a==y):
        print(y)
