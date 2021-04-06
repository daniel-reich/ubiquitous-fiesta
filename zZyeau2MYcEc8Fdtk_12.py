
def round_number(num, n):
    k = num // n
    if num%n >= n/2: return n*(k+1)
    else: return n*k

