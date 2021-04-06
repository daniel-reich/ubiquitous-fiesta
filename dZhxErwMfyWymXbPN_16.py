
def hangman(phrase, lst):
    return ''.join(l if l.lower() in lst else '-' if l.isalpha() else l for l in phrase)

