
def verbify(txt):
    j=txt.split()
    if j[0][-2:]=="ed":
        return txt
    elif j[0][-1]=="e":
        return j[0]+"d"+" "+j[1]
    else:
        return j[0]+"ed"+" "+j[1]

