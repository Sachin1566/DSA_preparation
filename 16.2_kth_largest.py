def kth_largest(arr, k):
    arr1=sorted(arr) 
    print(arr1)
    return arr1[n-k]
arr = [14, 56, 47,43,89,45,67,57,86]
n=len(arr)
k = 3
print(f"{k} largest element is",kth_largest(arr, k))  

