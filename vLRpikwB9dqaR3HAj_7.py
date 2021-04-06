
def is_ord_sub(smlst, biglst):
    a = 0
    for i in smlst:
        if i in biglst[a:]:
            a += biglst[a:].index(i) + 1
        else:
            return False
    return True

