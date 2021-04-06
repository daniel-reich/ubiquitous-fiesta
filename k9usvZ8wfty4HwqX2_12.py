
def cuban_prime(num):
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return '{} is not cuban prime'.format(num)
    disc = (3 ** 2 - 4 * 3 * (1 - num)) ** 0.5
    if disc % 1 == 0:
        return '{} is cuban prime'.format(num)
    return '{} is not cuban prime'.format(num)

