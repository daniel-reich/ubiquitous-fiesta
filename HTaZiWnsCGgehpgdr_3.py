
def license_plate(s, n):
    s = ''.join([c for c in s.upper() if c.isalpha() or c.isnumeric()])[::-1]
    end = len(s) // n if len(s) % n == 0 else len(s) // n + 1
    ans = '-'.join([s[k*n:k*n+n] for k in range(end)])
    return ans[::-1]

