
def pairs(lst, x = None):
    if x == None:
        x = []
    if len(lst) == 0:
        return x
    x.append([lst[0], lst[-1]])
    return pairs(lst[1:-1], x)

