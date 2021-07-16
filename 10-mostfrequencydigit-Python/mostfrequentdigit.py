# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
    # your code goes here
    p=[]
    if(len(str(n)==1)):
        return n
    elif(len(str(n)>1)):
        for i in str(n):
            if(i not in p):
                return 



