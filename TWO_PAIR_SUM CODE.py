#O(n)

# for(i=0,i<n;i++){
#     for(j=0;j<n;j++){
#         if(i==j)
#         continue;
#         if(arr[i]+arr[j]==target)
#     }
# }






# def two_sum(arr,target_sum):
#     left=0
#     right=len(arr)-1
#     while left< right:
#         if(arr[left]+ arr[right] == target_sum):
#             return left,right
#         elif(arr[left] + arr[right] < target_sum):
#             left=left+1
#         else:
#             right=right-1
#     return -1,-1
    
# #driver code

# # arr=[20,40,60,80,90,120,240]
# # target_sum=210   #(4,5)

# # arr=[2,7,11,15]
# # target_sum=9  #(0,1)

def two_sum(arr,target_sum):
        sums = {}
        for i , num in enumerate(nums):
            diff = target - num
            if diff in sums:
                return [sums[diff] , i]
            else:
                sums[num] = i
        return -1

nums=[3,2,4]
target=6  #[1,2]

result=two_sum(nums,target)
print(result)
            
