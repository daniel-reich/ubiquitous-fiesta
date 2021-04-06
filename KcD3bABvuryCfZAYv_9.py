
def most_frequent_char(lst):
    stringy = ""
    diccy  ={}
    seccy = {}
    for i in lst:
        for j in i:
            stringy = stringy + j
    setty = set(stringy)
    for p in setty:
        diccy[p] = stringy.count(p)
    revvy = {}
    for key, value in diccy.items():
        revvy[value] = revvy.get(value, []) + [key]
    #print(revvy)
    maxy = max(revvy)
    return sorted((revvy[maxy]))

