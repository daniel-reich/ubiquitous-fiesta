
def alternating_caps(txt):
    str_new, ind ='', 0
    for i in range(len(txt)):
        if ind == 0 and txt[i] != ' ':
            str_new = str_new + txt[i].upper()
            ind = 1
        elif ind == 1 and txt[i] != ' ':
            str_new = str_new + txt[i].lower()
            ind = 0
        else:
            str_new= str_new + ' '
            continue
    return str_new

