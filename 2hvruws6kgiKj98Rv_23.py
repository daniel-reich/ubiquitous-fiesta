
def to_scottish_screaming(txt):
    return ''.join('E' if x in 'aeiouAEIOU' else x for x in txt).upper()

