
def nearest_chapter(d, page):
    cop = d
    cop = {c:max(page,p)- min(page,p) for c,p in d.items()}
    if list(cop.values()).count(min(cop.values())) > 1:
        return [k for k,v in cop.items() if cop[k] < d[k]][-1]
    else:
        return min(cop,key=cop.get)

