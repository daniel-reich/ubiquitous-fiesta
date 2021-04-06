
def is_prime(primes, num, left=0, right=None):
    if num < 2 or num > 100:
        return "yes"
    right = len(primes) - 1
    not_guess = True
    while not_guess:
        if right < left:
            return "no"
        num1 = (round((left + right) / 2))
        if primes[num1] == num:
            return "yes"
        elif primes[num1] > num:
            right = num1 - 1
        else:
            left = num1 + 1

