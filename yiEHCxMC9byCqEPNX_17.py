
def is_palindrome(p):
    t = ''
    for i in p:
        if i.isalpha():
            t += i.lower()
    p = t
    if len(p) < 2:
        return True
    else:
        if p[0] == p[-1]:
            return is_palindrome(p[1:-1])
        else:
            return False

