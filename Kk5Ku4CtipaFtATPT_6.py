
def coconut_translator(txt):
    S = "coconuts"
    ans = []
    for c in txt:
        s = ""
        o = bin(ord(c))[2:].zfill(8)
        for i in range(8):
            if o[i] == '0':
                s += S[i].lower()
            else:
                s += S[i].upper()
        ans.append(s)
    return ' '.join(ans)

