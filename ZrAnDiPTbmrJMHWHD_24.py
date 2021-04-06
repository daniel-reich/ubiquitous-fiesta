
def is_central(txt):
    q, r = divmod(len(txt), 2)
    if r == 0:      return False
    return txt[q] != ' '

