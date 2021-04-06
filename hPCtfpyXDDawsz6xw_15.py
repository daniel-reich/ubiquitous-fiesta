
def verbify(txt):
    a = txt.split()
    if a[0][-2:] == "ed":
        return " ".join(a)
    return a[0] + "d" + " " + a[-1] if a[0][-1] == "e" else a[0] + "ed" + " " + a[-1]

