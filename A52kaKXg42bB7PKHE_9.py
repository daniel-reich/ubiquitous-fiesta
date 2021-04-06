
def num_then_char(lst):
    anz_listen = len(lst)
    elemente_in_listen = []
    for x in lst:
        elemente_in_listen.append(len(x))
    tmpn = []
    tmps = []
    for i in range(anz_listen):
        for j in range(len(lst[i])):
            if type(lst[i][j]) == str:
                tmps.append(lst[i][j])
            else:
                tmpn.append(lst[i][j])
    tmpn.sort()
    tmps.sort()
    tmpsumme = tmpn + tmps
    tagl = 0  # liest die aktuelle Liste
    tage = 0  # liest das aktuelle Element
    tl = []
    temp = []
    akt = 0
    for x in range(len(elemente_in_listen)):
        tl.clear()
        for y in range(elemente_in_listen[x]):
            tl.append(tmpsumme[akt])
            akt += 1
        temp.append(list(tl))
    return temp

