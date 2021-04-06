
def remove_repeats(txt):
    ret_txt = txt[0]
    for i, j in enumerate(txt[1:]):
        if txt[i] != j:
            ret_txt += j
    return ret_txt

