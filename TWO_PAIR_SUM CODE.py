#o(n)
def twosum(arr,i,j,target):
   
    
    while i<=j:
        if arr[i] + arr[j] == target:
            return [i,j]
        if arr[i] + arr[j]>target:
            j=j-1
        else:
            i=i-1
            
    return [-1,-1] #if its not found
    
arr=[2,7,11,15]
target=26
i=0
j=len(arr)-1
result=twosum(arr,i,j,target)
print(result)
