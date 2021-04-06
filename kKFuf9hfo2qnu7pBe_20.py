
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def is_prime(primes,x,left=0,right=None):
    for k in range(2,99):
        z=x%k
        if z==0:
            return "no"
        else:
            return "yes"

