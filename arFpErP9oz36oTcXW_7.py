
def secret(txt):
    txt = txt.split('.')
    return "<{} class=".format(txt[0]) + "'{}'".format(' '.join(txt[1:])) + '></{}>'.format(txt[0])

