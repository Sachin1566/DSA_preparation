# method - 1


# def kth_smallest(arr, k):
#     arr1=sorted(arr) 
#     print(arr1)
#     return arr1[k-1]

# method - 2

# import heapq

# def kth_smallest_element(arr, k):
   
#     return heapq.nsmallest(k, arr)[-1]  
    
    
#driver code

arr = [14, 56, 47,43,89,45,67,57,86]
n=len(arr)
k = 3
print(f"{k} smallest element is",kth_smallest(arr, k))  

