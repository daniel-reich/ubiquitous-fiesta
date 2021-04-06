
def keyboard_mistakes(txt):
    d = {'4':'A', '5':'S', '0':'O', '1':'I'}
    for k, v in d.items():
        txt = txt.replace(k,v)
    return txt

