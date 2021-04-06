
def cuban_prime(n):
    root = (3 + (12*n - 3)**0.5) / 6
    return '{} {} cuban prime'.format(n, 'is' if is_prime(n) and root == int(root) else 'is not')
  
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            return False
    return True

