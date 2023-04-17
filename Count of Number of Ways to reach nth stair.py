# Count of Number of Ways to reach nth stair
def posibilities(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return posibilities(n-1)+posibilities(n-2)
        
n=int(input())
result=posibilities(n)
print(result)