
def is_icecream_sandwich(txt):
    if txt == "" or txt.count(txt[0]) == len(txt): return False 
    a = ""
    for i in txt:
        if i == txt[0]:
            a += str(i)
        else:
            b = str(i)
            break
    res = [ele for ele in txt if(ele not in [txt[0], b])]
    if txt.count(a) == 2 and not res:
        return True
    return False

