
def repeated(s):
    return True if any(s[0:i] * n == s for i in range(1, len(s)) for n in range(2, (len(s)//i + 1))) else False

