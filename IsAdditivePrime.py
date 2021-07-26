def isPrime(n):
    if (n <= 1):
        return False
 
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
         
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
 
    return True
 
def getSum(n):
 
    sum = 0
    while (n != 0):
        sum = sum + n % 10
        n = n / 10
    return sum
def isAdditivePrime(n):
    if (not isPrime(n)):
        return False
    return isPrime(getSum(n))
print(isAdditivePrime(23))
# N = 23
 
# if (isAdditivePrime(N)):
#     print ("Yes")
# else:
#     print ("No")