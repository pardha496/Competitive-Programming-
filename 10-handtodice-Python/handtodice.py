# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
    # your code goes here
    p=[]#empty list
    #r=str(hand)#converting int to str for iteration
    while hand>0:
        i=hand%10#3
        hand=hand//10
        p.append(i)
    return(tuple(p[::-1]))

    # l = [int(i) for i in str(hand)]
    # print(tuple(l))

    
   
