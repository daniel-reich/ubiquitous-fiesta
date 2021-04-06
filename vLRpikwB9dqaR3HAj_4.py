
def is_ord_sub(smlst, biglst):
    a = biglst.index(smlst[0])
    if a is None or len(smlst) == len(biglst):
        return False
    for i in range(1, len(smlst)):
        biglst = biglst[a + 1::]
        if smlst[i] in biglst:
            a = biglst.index(smlst[i])
            continue
        else:
            break
    else:
        return True
    return False

