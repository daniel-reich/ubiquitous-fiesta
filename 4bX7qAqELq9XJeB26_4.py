
def to_camel_case(txt):
    if '-' in txt:
        return txt.split('-')[0] + ''.join(x.capitalize() for x in txt.split('-')[1:])
    else:
        return txt.split('_')[0] + ''.join(x.capitalize() for x in txt.split('_')[1:])

