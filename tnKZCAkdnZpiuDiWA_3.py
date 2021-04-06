
def flip_end_chars(txt):
    if type(txt) != str or len(txt) < 2:
        return 'Incompatible.'
    elif txt[0:1] == txt[-1:]:
        return "Two's a pair."
    else:
        txt = list(txt)
        txt[-1:], txt[0:1] = txt[0:1], txt[-1:]
        txt = ''.join(txt)
        return txt

