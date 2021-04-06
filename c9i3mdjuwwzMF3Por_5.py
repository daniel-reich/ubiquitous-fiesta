
def reverse(n):
    return int(str(n)[::-1])
​
def up_down(n):
    s = ''
    for i in str(n):
        s += '6' if i == '9' else '9' if i == '6' else i
    return int(s)
​
def isprime(n):
    return all( n % i for i in range(2,n//2+1))
​
def bemirp(n):
    if isprime(n):
        if n != reverse(n) and isprime(reverse(n)):
            if isprime(up_down(n)) and isprime(reverse(up_down(n))):
                return 'B'
            return 'E'
        return 'P'
    return 'C'

