
def validate_spelling(txt):
    L = txt.lower().replace('.', '').split()
    word = [c for c in L[-1] if c.isalpha()]
    return word == L[:-1]

