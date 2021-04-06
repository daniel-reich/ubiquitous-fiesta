
def is_ord_sub(smlst, biglst):
    if len(smlst) == 1:
        return smlst[0] in biglst
    elif smlst[0] not in biglst:
        return False
    else:
        return is_ord_sub(smlst[1:], biglst[biglst.index(smlst[0])+1:])

