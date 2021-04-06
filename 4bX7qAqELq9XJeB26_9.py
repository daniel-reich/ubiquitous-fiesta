
def to_camel_case(txt):
    if '_' in txt:
        txt = txt.split('_')
    else:
        txt = txt.split('-')
    return txt[0] + ''.join(x.title() for x in txt[1:])

