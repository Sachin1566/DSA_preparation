def collinear(x1, y1, x2, y2, x3, y3):
     
    #  method 1
 
    # a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
 
    # if (a == 0):
    #     print ("Yes")
    # else:
    #     print ("No")
    
    
    #method 2
    
    a=(y2-y1)*(x3-x2)
    b=(y3-y2)*(x1-x2)
    if(a==b):
        print("1")
    
    print("no")
    
    
# Driver Code
x1, x2, x3, y1, y2, y3 = 1, 2, 1, 1, 4, 5
collinear(x1, y1, x2, y2, x3, y3)