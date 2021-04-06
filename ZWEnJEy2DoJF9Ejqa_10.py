
def edabit_in_string(txt):
    x = list('edabit')
    s = []
    i = 0
    while i < len(txt) and x:
        if txt[i] == x[0]:
            s += [txt[i]]
            del x[0]
        i += 1
    if ''.join(s) == 'edabit':
        return 'YES'
    else:
        return 'NO'

