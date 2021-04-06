
def to_camel_case(txt):
    if '-' in txt:
        s = '-'
    else:
        s = '_'
    low = txt.split(s)
    return ''.join([low[i] if i==0 else low[i].capitalize() for i in range(len(low))])

