
def cap_last(s):
    lst = s.split(" ")
    newLst = []
    for w in lst:
        newLst.append(w[:len(w)-1] + w[len(w)-1].capitalize());
    return " ".join(newLst)

