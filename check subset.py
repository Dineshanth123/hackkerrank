n=int(input())
for x in range(n):
    a=int(input())
    i=set(map(int,input().split()))
    b=int(input())
    j=set(map(int,input().split()))
    if len(i-j)==0:
        print('True')
    else:
        print('False')
