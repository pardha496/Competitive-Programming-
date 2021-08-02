# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def TidyNumber(n):
    
    b=n%10
    n=n//10
    while (n>0):
        r=n%10
        if (r>b):
            return False
        b=r
        n=n//10
    return True
            
def nthTenlyPrime(n):
    n=abs(n)
    count=0
    i=1
    while (count<=n):
        if TidyNumber(i):
            count+=1
        i=i+1
    return i-1