
def pilish_string(txt):
    p = str(314159265358979)
    r = ""
    for x in p:
        if txt:
            part = txt[: int(x)]
            if len(part) < int(x):
                part += part[-1] * (int(x) - len(part))
            r += part + " "
            txt = txt[int(x) :]
        else:
            break
    return r[:-1]

