
def funny_numbers(n, p):
    digits = [int(_) for _ in str(n)]
    m = sum([digits[i]**(p+i) for i in range(len(digits))])
    return (m // n) if m % n == 0 else None

