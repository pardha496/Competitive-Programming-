# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    
    x = abs(n)
    p = -1
    while(x>0):
        r = x%10
        x = x//10
        if(r==p):
            return True
        p = r
    return False