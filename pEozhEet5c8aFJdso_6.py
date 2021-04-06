
def all_about_strings(txt):
    mid = txt[(len(txt)-1)//2:(len(txt)+2)//2]
    lst = [len(txt), txt[0], txt[-1], mid]
    if txt[1] in txt[2:]:
        x = txt.index(txt[1],2)
        lst.append('@ index {}'.format(x))
    else:
        lst.append('not found')
    return lst

