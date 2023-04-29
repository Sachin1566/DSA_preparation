#A peak element is an element that is strictly greater than its neighbors.

#Given a 0-indexed integer array nums, find a peak element, and return its index. 
#If the array contains multiple peaks, return the index to any of the peaks.
#Example 1:

#Input: nums = [1,2,3,1]
#Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

#method
#tc=O(log n)
def peak_element(nums):
    start,end=0,len(nums)-1
    
    if nums[0]>nums[1]:
        return 0
        
    if nums[-1]>nums[-2]:
        return len(nums)-1
        
    while start<end: #modified binary search
        mid=start+(end-start)//2
        
        if nums[mid]< nums[mid+1]:
            start=mid+1
        else:
            end=mid
            
    return end
            
        
        
#driver code
# nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
print(peak_element(nums))