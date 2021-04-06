
def is_exactly_three(n):
    for i in range (2,n-1):
        if (n%i==0):
            return (i*i==n)
    return False
            
# if n is a square of a prime number then true else false

