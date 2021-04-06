
def is_ord_sub(smlst, biglst):
    i, j = 0, 0
    while i < len(smlst) and j < len(biglst):
        if smlst[i] == biglst[j]:
            i += 1
        j += 1
    return i == len(smlst)

