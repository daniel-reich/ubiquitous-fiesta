
def unstretch(word):
    from itertools import groupby
    return ''.join(k for k, g in groupby(word))

