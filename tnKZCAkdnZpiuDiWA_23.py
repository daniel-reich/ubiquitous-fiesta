
def flip_end_chars(txt):
    if len(txt) < 2 or type(txt) != str:
        return "Incompatible."
    if txt[0] == txt[-1]:
        return "Two's a pair."
    return txt[-1] + txt[1:-1] + txt[0]

