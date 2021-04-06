
def make_change(c):
    q = int(c/25)
    d = int((c-(q*25))/10)
    n = int((c-(q*25+d*10))/5)
    p = int((c-(q*25+d*10+n*5)))
    return {"q": q, "d": d, "n": n, "p": p}

