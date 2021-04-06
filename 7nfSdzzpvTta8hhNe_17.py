
def organize(txt):
    if not txt:
        return {}
    else:
        d = {}
        s = txt.split(",")
        s[-1] = s[-1][1:]
        d.update({"name": s[0]})
        d.update({"age": int(s[1])})
        d.update({"occupation": s[-1]})
        return d

