
def direction(lst):
    r = []
    x = "eastEAST"
    y = "westWEST"
    for i in lst:
        table = i.maketrans(x, y)  
        r.append(i.translate(table))
    return r

