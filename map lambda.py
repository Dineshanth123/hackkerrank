cube = lambda x: x*x*x 

def fibonacci(n):
    l=[0,1]
    for x in range(2,n):
        l.append(l[x-1]+l[x-2])
    return (l[0:n])
    


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))