
def is_prime(n):
    if n < 4 or n%2 == 0: return n == 2 or n == 3
    for i in range(3, 1+int(n**0.5), 2):
        if n%i == 0: return False
    return True
​
def cuban_prime(num):
    if is_prime(num):
        y, p = 1, 0
        while p < num:
            p = (y+1)**3 - y**3
            if p == num:
                return str(num) + " is cuban prime"
            y += 1  
    return str(num) + " is not cuban prime"

