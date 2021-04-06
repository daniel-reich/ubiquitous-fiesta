
def duplicates(s):
    g = 0
    b = set(s)
    for x in b:
        if len(s)-len(s.replace(x, "")) > 1:
            g = g + (len(s) - len(s.replace(x, "")) - 1)
    return(g)

