# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
    # Your code goes here
    li=[]
    count=0
    for i in range(len(L)):
        for j in range(len(L[i])):
            li.append(L[i][j])
    for i in range(len(L)):
        for j in range(len(L[i])):
            l1=li[:]
            l1.remove(L[i][j])
            if((L[i][j]) in l1):
                return True
    return False
