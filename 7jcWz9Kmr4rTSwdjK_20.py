
def is_prime(x):
    for i in range(2,x-1):
        if x % i == 0:
            return False
    return True
​
def prime_factorize(num):
    temp = num
    factor_list = []
    counter = 2
    while counter <= num:
        if num % counter == 0 and is_prime(counter):
            factor_list.append(counter)
            num //= counter
            counter = 2
            continue
        counter += 1
    return factor_list

