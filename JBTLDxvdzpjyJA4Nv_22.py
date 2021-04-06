
def super_reduced_string(txt):
    last = txt
    while True:
        for i in set(txt):
            if i + i in txt:
                txt = txt.replace(i + i, "")
        if txt == last:
            break
        else:
            last = txt
    if txt:
        return txt
    return "Empty String"

