
def prime_numbers(num):
    count = 0
    for i in range(num+1):
        if prime(i):
            count += 1
    return count
​
​
def prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True

