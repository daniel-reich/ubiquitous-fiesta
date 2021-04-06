
def unmix(txt):
    j = [txt[i:i+2][::-1] for i in range(0, len(txt), 2)]
    return "".join(j)

