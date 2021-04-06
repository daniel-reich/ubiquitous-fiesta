
def negative_sum(chars):
    r, add = [], "-"
    while "-" in chars:
        s = chars.index("-")
        chars = chars[s:]
        s = 0
        while s + 1 < len(chars) and chars[s + 1].isnumeric(): 
            s += 1
        add = int(chars[: s + 1])
        r.append(add)
        add = "-"
        chars = chars[s + 1 :]   
    return sum(r)

