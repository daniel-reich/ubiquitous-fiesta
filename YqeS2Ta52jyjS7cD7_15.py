
def is_prime(n):
    n = abs(n)
    answer = 0
    if n < 2:
        return False
    for i in range(1, n):
        if n % i == 0:
            answer = answer +1
            
            
    return False if answer > 1 else True

