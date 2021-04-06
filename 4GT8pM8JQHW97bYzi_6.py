
import math
def check_prime(n):
    if n <= 0:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
​
​
​
def loneliest_number(lo, hi):
    number = 0
    distance = 0
    closest = 0
    for num in range(lo, hi + 1):
        if lo == 0:
            number = 0
            distance = 2
            closest = 2
        i = 1
        while not check_prime(num - i) and not check_prime(num + i):
            i += 1
            if (check_prime(num - i) and check_prime(num + i)) or (not check_prime(num - i) and check_prime(num + i)):
                if i > distance:
                    number = num
                    distance = i
                    closest = num + i
            elif check_prime(num - i) and not check_prime(num + i):
                if i > distance:
                    number = num
                    distance = i
                    closest = num - i
​
    return {"number": number, "distance": distance, "closest": closest}

