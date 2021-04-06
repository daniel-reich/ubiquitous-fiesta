
def is_palindrome(p,normal = False):
    if not normal:
        p = ''.join(i.lower() for i in p if i.isalpha())
    if len(p) == 1 or len(p) == 0:
        return True
    if p[0] != p[-1]:
        return False
    if p[0] == p[-1]:
        return is_palindrome(p[1:-1],True)

