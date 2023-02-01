# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
x=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
y=[y for y in x if y in A]
i=len(y)
z=[z for z in x if z in B]
j=len(z)
k=i-j
print(k)
        
