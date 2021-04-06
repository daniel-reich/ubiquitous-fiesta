
def word_to_decimal(word):
    lst = [ord(c) - 96 for c in word.lower()]
    base = 10 + max(lst)
    return sum((9 + v) * pow(base, i) for i, v in enumerate(lst[::-1]))

