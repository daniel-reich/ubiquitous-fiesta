
def edabit_in_string(txt):
    test = 'edabit'
    res = ''
    idx_start = -1
    for c in test:
        idx_start = txt.find(c, idx_start+1)
        if idx_start > -1:
            res += c
        else:
            break
            
    return 'YES' if test == res else 'NO'

