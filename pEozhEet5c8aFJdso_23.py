
def all_about_strings(txt):
    l = len(txt)
    a = txt[0]
    z = txt[-1]
    t = txt[1]
    if l%2 == 0:
        m = txt[(l//2)-1] + txt[l//2] 
    if l%2 != 0:
        m = txt[l//2]
    if txt.count(t) > 1:
        s = '@ index ' + str(txt.index(t,2))
    if txt.count(t) == 1:
        s = "not found"
    return [l, a, z, m, s]

