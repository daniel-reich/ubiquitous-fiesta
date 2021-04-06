
def shift_letters(txt, n):
    letters = txt.replace(' ', '')
    n %= len(letters)
    shifted = iter((letters[-n:] + letters[:-n]))
    return ''.join(' ' if i.isspace() else next(shifted) for i in txt)

