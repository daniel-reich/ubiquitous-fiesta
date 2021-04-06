
def c_prime(y):
    x = y+1
    p = int((x**3-y**3)/(x-y))
    for i in range(2, p):
        if p % i == 0:
            x += 1
            y += 1
            p = int((x**3-y**3)/(x-y))
            continue 
    return p
​
def cuban_prime(num):
    for numbers in range(1, num):
        if c_prime(numbers) > num:
            break
        if c_prime(numbers) == num:
            return str(num) + " is cuban prime"
    return str(num) + " is not cuban prime"

