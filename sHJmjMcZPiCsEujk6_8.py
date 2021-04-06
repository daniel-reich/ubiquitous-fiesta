
def pilish_string(txt):
    pi = "314159265358979"
    curr_id = 0
    res = ""
    for i in pi:
        if curr_id >= len(txt)  :
            break
        if len(txt[curr_id:]) >= int(i):
            res += txt[curr_id:curr_id + int(i)] + " "
        else:
            res += txt[curr_id:] + (int(i) - len(txt[curr_id:]))*txt[-1]
            break
        curr_id += int(i)
    return res.strip()

