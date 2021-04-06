
def reverse_odd(txt):
    return ' '.join([s[::-1] if len(s)%2 else s for s in txt.split()])

