def average(array):
    
    y=set(array)
    x=sum(y)
    n=len(set(arr))
    result=x/n
    return result
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

