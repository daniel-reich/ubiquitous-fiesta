
def valid_name(k):
    lists = k.split()
    if len(lists) == 1:
        return False
    if len(lists[len(lists)-1]) < 3:
        return False
    if len(lists) > 3:
        return False
    for i in range(0,len(lists)):
        Kontrolle = list(lists[i])
        if len(Kontrolle) == 1:
            return False
        elif len(Kontrolle) != 2 and Kontrolle[len(Kontrolle)-1]==".":
            return False
        if Kontrolle[0].islower() == True:
            return False
        try:
            if len(Kontrolle) == 2 and len(list(lists[i+1])) > 2 and len(list(lists[i+2])) >2:
                return False
        except:
            continue
    return True

