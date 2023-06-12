l=list(map(int,input("enter number").split()))
result=all(l[i]<l[i+1] for i in range(len(l)-1))
print("ascending" if result==True else "not ascending")
