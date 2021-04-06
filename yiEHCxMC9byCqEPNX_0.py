
def is_palindrome(p):
    p = ''.join([i.lower() for i in p if i.isalpha()])
    if len(p) < 2:
        return True
    else:
        return is_palindrome(p[1:-1]) if p[0] == p[-1] else False

