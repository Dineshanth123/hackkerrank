T = int(input())
for z in range(T):
    a = int(input())
    x = [int(x) for x in input().split()]
    left = 0
    right = a - 1
    l = []
    while left < right:
        if x[left] >= x[right]:
            l.append(x[left])
            left += 1
        else:
            l.append(x[right])
            right -= 1
    result = all(l[i] >= l[i+1] for i in range(len(l)-1))
    if result:
        print("Yes")
    else:
        print("No")
