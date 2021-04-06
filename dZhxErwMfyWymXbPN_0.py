
def hangman(s, l):
    return ''.join('-' if x.isalpha() and x.lower() not in l else x for x in s)

