
def censor(s):
    lst = []
    for e in s.split(" "):
        if not len(e) > 4:
            lst.append(e)
        else:
            lst.append("*" * len(e))
    return " ".join(lst)

