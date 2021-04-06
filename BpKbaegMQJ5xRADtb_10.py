
def isprime(n):
    return False if n <= 1 else all(n % i for i in range(2,n//2+1))
​
def rid_zero(s):
    while len(s) >= 2 and s[0] == '0':
        s = s[1:]
    return s
​
def is_unprimeable(n):
    if isprime(n):
        return 'Prime Input'
    else:
        s = str(n)
        lst = [s[:i]+str(j)+s[i+1:] for i in range(0,len(s)) for j in range(10) ]
        lst[0] = rid_zero(lst[0])
        prime_list = [int(i) for i in lst if isprime(int(i))]
        return 'Unprimeable' if not prime_list else sorted(prime_list)

