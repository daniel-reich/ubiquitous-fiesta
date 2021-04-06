
def swap_xy(txt):
    str1 = txt[txt.index('(') + 1 : txt.index(',')]
    str2 = txt[txt.index(',') + 2 : txt.index(')')]
    str3 = txt[txt.rindex('(') + 1 : txt.rindex(',')]
    str4 = txt[txt.rindex(',') + 2 : txt.rindex(')')]
    return '({}, {}), ({}, {})'.format(str2, str1, str4, str3)

