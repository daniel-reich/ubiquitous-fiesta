
def binary_to_decimal(lst):
    newlst = []
    for x in lst:
        newlst.append(str(x))
    a = "".join(newlst)
    return int(a, 2)

