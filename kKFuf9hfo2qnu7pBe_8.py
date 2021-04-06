
def is_prime(primes, num, left=0, right=None):
 primes1 = primes
 while 1:
    print(primes1)
    if len(primes1) == 1:
        break
    if num < primes1[round(len(primes1) / 2)-1]:
        primes1 = primes1[:round(len(primes1) / 2)]
    elif num > primes1[round(len(primes1) / 2)-1]:
        primes1 = primes1[round(len(primes1) / 2):len(primes1)]
    elif num == primes1[round(len(primes1) / 2)-1]:
        return 'yes'
​
 if num == primes1:
    return 'yes'
 else:
    return 'no'
​
A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(is_prime(A, 11))

