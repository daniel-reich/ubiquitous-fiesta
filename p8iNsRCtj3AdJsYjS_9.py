
def title_to_number(s):
    return sum((ord(i) - 64) * 26**idx for idx, i in enumerate(s[::-1]))

