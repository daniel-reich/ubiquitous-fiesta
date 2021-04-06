
def truncate(txt, length):
    c = ' '
    txt = txt + c
    master = [pos for pos, char in enumerate(txt) if char == c]
    if length in master:
        return txt[0:length]
    else:
        new_list = sorted(master + [length])
        offst = new_list.index(length)
        if offst == 0:
            return ""
        else:
            offst -= 1
            new_index = new_list[offst]
            return txt[0:new_index]

