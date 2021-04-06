
def organize(txt):
    if len(txt)==0:return {}
    txt = txt.split(', ')
    return {'name':txt[0], 'age':int(txt[1]), 'occupation':txt[2]}

