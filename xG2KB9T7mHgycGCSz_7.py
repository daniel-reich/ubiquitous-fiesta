
def valid(txt):
    return (len(txt)==4 or len(txt)==6) and all([i.isdigit() for i in txt])

