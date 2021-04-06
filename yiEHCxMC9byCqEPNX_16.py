
def is_palindrome(p):
    import string
    p = p.translate(str.maketrans('', '', string.punctuation + string.whitespace)).lower()
    print(p)
    if len(p) <= 1:
        return True
    else:
        return p[0] == p[-1] and is_palindrome(p[1:-1])

