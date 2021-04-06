
def magic(txt):
    m, d, y = txt.split(); md = str(int(m) * int(d))
    return md == str(y)[-len(md):]

