
def secret(txt):
    txt = txt.split('.')
    return  "<{0} class='{1}'></{0}>".format(txt[0],' '.join(txt[1:]))

