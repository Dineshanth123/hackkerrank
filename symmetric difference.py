M=int(input())
s1=set(map(int,input().split()))
N=int(input())
s2=set(map(int,input().split()))
s3=sorted(s1^s2)
for x in s3:
    print(x)