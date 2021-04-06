
def color_conversion(h):
    if type(h) == dict:
        for i in h:
            if h[i] < 0 or h[i] > 255:
                return "Invalid input!"
        r = hex(h["r"])[2:]
        g = hex(h["g"])[2:]
        b = hex(h["b"])[2:]
        return "#{}{}{}".format(r.zfill(2), g.zfill(2), b.zfill(2))
    else:
        ok = "1234567890abcdef"
        h = h.replace("#", "")
        if not all([i in ok for i in h]) or len(h) != 6:
            return "Invalid input!"
        r = int(h[:2], 16)
        g = int(h[2:4], 16)
        b = int(h[4:], 16)
        return {"r" : r, "g" : g, "b" : b}

