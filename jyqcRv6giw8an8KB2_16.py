
def invert(s):
    return ''.join(i.upper() if i.islower() else i.lower() for i in s[::-1])

