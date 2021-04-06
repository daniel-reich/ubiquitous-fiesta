
def secret(txt):
    txt = txt.split('.')
    tag = txt.pop(0)
    return "<" + tag + " class='" + ' '.join(txt) + "'></" + tag + ">"

