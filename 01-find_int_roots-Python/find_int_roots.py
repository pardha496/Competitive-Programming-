# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
  
  
# function for finding roots
def fun_find_int_roots( a, b, c): 
  
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    # checking condition for discriminant
    if dis > 0: 
    
        return((-b + sqrt_val)/(2 * a)) 
        return((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        
        return(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        
        return(- b / (2 * a), " + i", sqrt_val) 
        return(- b / (2 * a), " - i", sqrt_val)




