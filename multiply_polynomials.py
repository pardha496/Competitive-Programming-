# Background: we can represent a polynomial as a list of its coefficients. 
# For example, [2, 3, 0, 4] could represent the polynomial 2x3 + 3x2 + 4. 
# Write the function multiplyPolynomials(p1, p2) which takes two polynomials 
# and returns a third polynomial which is the product of the two. For example,
# multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 5), and:
# (2x**22 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns [8, 10, 12, 15].

def multiplyPolynomial(p1, p2):
    x=len(p1)
    y=len(p2)
    product = []
    product_length = x + y - 1
    for i in range(product_length):
        product.append(0)
    for i in range(x):
        for j in range(y):
            product[i + j] += p1[i] * p2[j] 

    print (product) 

multiplyPolynomial([2,0,3], [4,5])