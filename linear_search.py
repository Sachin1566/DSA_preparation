def linear_search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

arr=[int(x) for x in input().split()]
print(linear_search(arr))