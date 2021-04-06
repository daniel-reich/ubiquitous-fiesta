
def all_about_strings(txt):
    l = len(txt) // 2
    a = ''
    if txt.count(txt[1]) >= 2:
        a = '@ index ' + str(txt.rindex(txt[1]))
    else:
        a = 'not found'
    if len(txt) % 2 != 0:
            return [len(txt), txt[0], txt[-1], txt[l], a]
    return [len(txt), txt[0], txt[-1], txt[l-1:l+1], a]

