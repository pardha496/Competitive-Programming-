# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricexcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards).
# Hint: you may want to use fabricyards, which you just wrote!


def fabricyards(inches):
    # Your code goes here...
    if(inches==0):
        return 0
    elif(inches>0 and inches<=36):
        return 1
    elif(inches>36):
        x=inches//36
        if(inches%36==0):
            return x
        else:
            return x+1

def fabricexcess(inches):
    # Your code goes here...
    if(inches==0 or inches==36):
        return 0
    elif(inches>=1 and inches<36):
        x=36-inches
        return x
    else:
        if(inches%36==0):
            return 0
        else:
            x=inches%36
            y=36-x
            return y