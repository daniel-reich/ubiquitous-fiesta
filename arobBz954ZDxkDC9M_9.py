
def next_prime(num):
    while True:
        if is_prime(num):
            return num
        num += 1
    
def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

