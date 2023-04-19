# implementation of randomizedpartition
import random

def randomizedpartition(arr,p,q):
    #callling rand pivot 
    randomPivotIndex=random.randrange(p,q)
    #swap the random index with first index
    arr[p],arr[randomPivotIndex]=arr[randomPivotIndex],arr[p]
    return partition(arr,p,q)


## method defination of partition

def partition(arr,p,q):
    pivot=arr[p]
    i=p
    for j in range(i+1,q+1):
        if arr[j]<=pivot:
            i += 1
            #swap between the vales of arr[i] and arr[j]
            arr[i],arr[j]=arr[j], arr[i]
    #final swap between the vales of arr[i] and arr[p]
    arr[i], arr[p]=arr[p],arr[i]
    return i
        

#method defination of quick sort

def quicksort(arr,p,q):
    if p<q:
        #divide and conquer
        #1.divide
        #function callling for the partition method
        mid=randomizedpartition(arr,p,q)
        #recursive   function call for the left subtree
        quicksort(arr,p, mid-1)
        #recursive   function call for the rightsubtree
        quicksort(arr,mid+1, q)
        
    return arr

#driver code
arr=[50,70,29,67,12,15,46,97,57,44]
p=0
q=len(arr)-1
#function callling
result=quicksort(arr,p,q) 
print(result)


