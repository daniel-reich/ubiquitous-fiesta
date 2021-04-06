
def simplify(txt):
    splitTxt = txt.split("/")
    numer = int(splitTxt[0])
    denom = int(splitTxt[1])
    if numer % denom == 0:
        return str(round(numer/denom))
    else:
        gcd = round(max([numer, denom])/2)
        while gcd > 1:
            if numer % gcd == 0 and denom % gcd == 0:
                return str(round(numer/gcd)) + "/" + str(round(denom/gcd))
            gcd-=1
        return txt

