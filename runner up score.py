if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    y=list(set(sorted(arr)))
    x=y[len(y)-2]
    print(x)
    