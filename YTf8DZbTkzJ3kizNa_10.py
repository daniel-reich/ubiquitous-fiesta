
def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for num_1 in range(2, num // 2 + 1):
        if num % num_1 == 0:
            return False
    return True
​
def moran(n):
    if (n % sum(int(num) for num in str(n))) == 0 and is_prime(n // sum(int(num) for num in str(n))):
        return "M"
    elif (n % sum(int(num) for num in str(n))) == 0 and not is_prime(n // sum(int(num) for num in str(n))):
        return "H"
    else:
        return "Neither"

