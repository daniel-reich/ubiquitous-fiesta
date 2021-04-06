
def alphabet_index(txt):
    return " ".join([str(ord(t.upper())-64) for t in txt if t.isalpha()])

