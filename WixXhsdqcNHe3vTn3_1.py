
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True
​
def how_bad(n):
    ones, res = bin(n).count('1'), [] 
    if ones%2:
        res.append('Odious')
    else:
        res.append('Evil')
    if is_prime(ones):
        res.append('Pernicious')
    return res

