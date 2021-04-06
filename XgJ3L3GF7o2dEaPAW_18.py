
def shared_letters(a, b):
    a = a.lower()
    b = b.lower()
    txt = ""
    a_set = set(a)
    for i in a_set:
        if i in b:
            txt += i
    return("".join(sorted(txt)))

