
def shift_sentence(txt):
    words = txt.split()
    return ' '.join(a[0] +b[1:] for a, b in zip(words[-1:] + words[:-1], words))

