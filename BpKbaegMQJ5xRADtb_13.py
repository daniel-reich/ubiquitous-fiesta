
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            return False
    return True
​
def is_unprimeable(n):
    if is_prime(n):
        return 'Prime Input'
    
    s, changes = str(n), set()
    for pos in range(len(s)):
        for d in '0123456789':
            new = int(s[:pos] + d + s[pos+1:])
            if is_prime(new):
                changes.add(new)
    
    return sorted(changes) if changes else 'Unprimeable'

