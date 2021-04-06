
def is_prime(n):
    return n > 1 and (n == 2 or (n%2 != 0 and all(n%ii for ii in range(3, int(n**0.5 + 1), 2))))
​
def bemirp(n):
    if not is_prime(n): return 'C'  # non-prime 
    sn = str(n)
    rsn = sn[::-1]
    if sn == rsn or not is_prime(int(rsn)): return 'P'  # palindromic prime or not emirp
    usn = ''.join(['9' if c == '6' else '6' if c == '9' else c for c in sn])
    return 'B' if is_prime(int(usn)) and is_prime(int(usn[::-1])) else 'E' # bemirp or emirp

