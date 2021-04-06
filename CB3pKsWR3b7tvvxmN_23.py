
def is_palindrome(txt):
 t = ''.join(c.lower() for c in txt if c.isalpha())
 return t == t[::-1]

