
from random import randint
​
def is_prime(num, trials=100):
    return all(pow(randint(2, num - 1), num - 1, num) == 1 for i in range(trials))

