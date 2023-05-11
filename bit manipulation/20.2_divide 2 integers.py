# approach-1- for large number some cases are failed


# def divide(divident,divisor):
#     count=0
#     while divident>=divisor:
#         divident -=divisor
#         count+=1 
#     print(count)
    
    
# divide(47,4)

# approach-2 optimized using bit manipulation



## Method definition
def divide(dividend, divisor):
  divid = abs(dividend)
  div = abs(divisor)
  result = 0
        
  while divid >= div:
    shift = 0 # bcz for every iteration i'm starting from scratch 
  ## left shift operator
    while divid >= (div << shift):
      shift += 1
            
      result += (1 << (shift - 1))
      divid -= div << (shift - 1)
            
  ## negative case handling
      if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):
        result = -result
        
  return min(2147483647, max(-2147483648, result))

## Driver code
dividend = 47
divisor = 4
result = divide(dividend, divisor)
print(result)