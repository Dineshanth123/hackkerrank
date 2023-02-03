n=int(input())
a=set(map(int,input().split()))
s=int(input())
b=set(map(int,input().split()))
s1=a^b
print(len(s1))