# https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import heappush, heappop
import math
## function definition
## get_dist is to give the euclidean distance
def get_dist(x,y):
    return math.sqrt(x**2 + y**2)

def kClosest(points, k):
    min_heap = []
    n = len(points)
    for i in range(n):
        x = points[i][0]
        y = points[i][1]
        ## to insert the elements inside the minheap
        heappush(min_heap, (get_dist(x,y), points[i]))
        
    result = []
    for i in range(k):
        ## to delete the elements from the minheap
        result.append(heappop(min_heap)[1])
    return result

## Driver code
points = [[3,3], [5,-1], [-2, 4]]
k = 2
## function calling
result = kClosest(points, k)
print("K Closest Points to the origin are:",result)