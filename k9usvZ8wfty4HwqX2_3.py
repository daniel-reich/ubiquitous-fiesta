
def cuban_prime(num):
    if not is_prime(num):
        return str(num) + ' is not cuban prime'
    y = 1
    while True:
        x = 3*(y**2) + 3*y + 1
        if x == num:
            return str(num) + ' is cuban prime'
        if x > num:
            return str(num) + ' is not cuban prime'
        y += 1
        
​
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

