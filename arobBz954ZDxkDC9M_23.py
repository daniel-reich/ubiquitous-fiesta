
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
​
​
def next_prime(num):
    if is_prime(num):
        return num
    for x in range(num, num+num//2):
        if is_prime(x):
            return x

