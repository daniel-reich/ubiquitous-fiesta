
def is_palindrome(p):
    p = ''.join([c for c in p.lower() if 'a' <= c <= 'z'])
    n = len(p)
    if n <= 1:
        return True
    if p[0] != p[-1]:
        return False
    return is_palindrome(p[1:-1])

