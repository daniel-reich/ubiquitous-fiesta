
def title_to_number(s):
    return sum(pow(26, i) * (ord(c) - 64) for i, c in enumerate(s[::-1]))

