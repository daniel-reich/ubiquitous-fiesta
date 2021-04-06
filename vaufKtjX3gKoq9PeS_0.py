
def ohms_law(u, r, i):
    if (u, r, i).count(None) != 1:
        return "Invalid"
    elif u is None:
        return r * i
    elif r is None:
        return u / i
    elif i is None:
        return round(u / r, 2)

