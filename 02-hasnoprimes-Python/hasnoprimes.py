# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
    # your code goes here
    for row in range(len(l)):
        for col in range(len(l[row])):
             
            b=prime(l[row] [col])
            if (b == True):
                return False
    return True

def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
            
        

        return True
    else:
        return False
        #return True

