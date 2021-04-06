
def get_prices(l):
    r=[]
    for s in l:
        r.append(float((s[s.find("($")+1:s.find(")")].replace("$",""))))
    return r

