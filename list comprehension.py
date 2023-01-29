if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a=[p for p in range(x+1)]
    b=[q for q in range(y+1)]
    c=[r for r in range(z+1)]
    s=[[i,j,k] for i in a for j in b for k in c]
    result=[t for t in s if sum(t)!=n]
    print(result)
    