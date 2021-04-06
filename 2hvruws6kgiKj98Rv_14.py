
def to_scottish_screaming(txt):
    return "".join([i.upper() if i not in 'aiou' else 'E' for i in txt.lower()])

