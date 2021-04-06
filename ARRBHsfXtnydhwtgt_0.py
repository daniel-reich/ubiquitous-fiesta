
def compress(c, acc = ""):
    if c == []: return acc
    ch, ix, limit = c[0], 0, len(c)
    while ix < limit and c[ix] == ch:
       ix += 1
    acc += ch + ("" if ix == 1 else str(ix))
    return compress(c[ix:], acc)

