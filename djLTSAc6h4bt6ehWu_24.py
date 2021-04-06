
def camelCasing(txt):
    if '_' in txt:
        txt = txt.replace('_', ' ')
    txt = txt.split()
    lst = [txt[0].lower()]
    for i in txt[1:]:
        lst.append(i.capitalize())
    return ''.join(lst)

