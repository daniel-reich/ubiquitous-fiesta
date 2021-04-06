
def min_removals(txt1, txt2):
    count = 0
    if len(txt1) < len(txt2):
        txt1, txt2 = txt2, txt1
    for i in txt2:
        if i not in txt1:
            txt2 = txt2.replace(i,'')
            count += 1
    return len(txt1) - len(txt2) + count

