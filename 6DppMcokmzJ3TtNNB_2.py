
def true_alphabetic(txt):
    letters = iter(i for i in sorted(txt) if i.isalpha())
    return ''.join(next(letters) if i.isalpha() else ' ' for i in txt)

