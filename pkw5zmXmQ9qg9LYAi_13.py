
def eval_bracket(txt):
    cnt = ""
    while '0' <= txt[0] <= '9':
        cnt += txt[0]
        txt = txt[1:]
    return txt * int(cnt)
​
def space_message(txt):
    if ']' not in txt:
        return txt
    idx2 = txt.find(']')
    idx1 = idx2 - 1
    while idx1 > 0 and txt[idx1] != '[':
        idx1 -= 1
    txt = txt[:idx1] + eval_bracket(txt[idx1+1:idx2]) + txt[idx2+1:]
    return space_message(txt)

