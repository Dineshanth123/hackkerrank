a,b,c=map(int,input().split())
if(a+b>c and b+c>a and a+c>b):
    print("it forms triangle")
else:
    print("not forms a triangle")
