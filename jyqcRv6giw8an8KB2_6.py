
def invert(s):
    return ''.join(letter.upper() if letter.islower() else letter.lower() for letter in s[::-1])

