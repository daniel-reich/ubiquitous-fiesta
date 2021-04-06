
def ohms_law(u, r, i):
    if (u and r and i):
        return 'Invalid'
    elif (u and i):
        return round(u / i, 2)
    elif (r and i):
        return r * i
    elif (u and r):
        return round(u / r, 2)
    else:
        return "Invalid"

