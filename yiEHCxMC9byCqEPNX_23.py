
def is_palindrome(p):
    if len(p) == 0:
        return True
    if not p[0].isalnum():
        return is_palindrome(p[1:])
    if not p[-1].isalnum():
        return is_palindrome(p[:-1])
    if p[0].lower() != p[-1].lower():
        return False
    return is_palindrome(p[1:-1])

