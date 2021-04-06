
def next_prime(num):
    for i in range(2, num):
        if num % i == 0:
            num += 1
            return next_prime(num)
    else:
        return num

