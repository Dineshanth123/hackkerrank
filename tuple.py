if __name__ == '__main__':
    n = int(input())
    t= map(int, input().split())
    print(hash(tuple(t)))
