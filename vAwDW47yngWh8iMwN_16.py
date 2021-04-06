
def cap_last(txt):
    return " ".join([x[:-1] + x[-1].upper() for x in txt.split()])

