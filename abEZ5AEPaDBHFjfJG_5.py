
def formula(txt):
    if txt == '':
        return None
    txt = txt.replace('a', '4')
    lst = txt.split('=')
    return len(set([eval(x) for x in lst])) == 1

