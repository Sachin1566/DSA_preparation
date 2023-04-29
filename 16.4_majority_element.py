#method
#TC=O(N)
#SC=O(N) BCZ CREATING DICTIONARY
from collections import Counter
def majority_element(nums):
    counts=Counter(nums)
    print(counts)
    return max(counts.keys(),key=counts.get)

#driver code
nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))