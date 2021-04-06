
def secret(txt):
    a, *b = txt.split(".")
    return "<{} class='{}'></{}>".format(a, " ".join(b), a)

