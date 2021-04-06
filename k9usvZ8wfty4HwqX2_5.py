
def is_prime(n):
    return all(n % num for num in range(2, int(n**0.5)+1)) and n > 1
​
​
def cuban_prime(num):
    return "{} is cuban prime".format(num) if is_prime(num) and (3 + (12 * num - 3)**.5) % 6 == 0 else "{} is not cuban prime".format(num)

