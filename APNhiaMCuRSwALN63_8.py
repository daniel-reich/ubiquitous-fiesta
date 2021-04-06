
def almost_palindrome(txt):
    rev = txt[::-1]
    n = 0
    for i in range(len(txt)):
        if txt[i] != rev[i]:
            n += 1
    else:
        if n == 2:
            return True
        else:
            return False

