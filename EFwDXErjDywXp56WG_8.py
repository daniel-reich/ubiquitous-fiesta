
def is_in_order(txt):
    y=list(txt)
    h=[i for i in txt]
    h.sort()
    return y==h

