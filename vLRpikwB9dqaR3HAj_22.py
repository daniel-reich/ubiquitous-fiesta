
def is_ord_sub(smlst, biglst):
    order = 0
    ans = []
    for i in range(len(smlst)):
        for j in range(order,len(biglst)):
            if biglst[j] == smlst[i]:
                order = j+1
                ans.append(j)
                break
    if len(ans) == len(smlst):
        return True
    else:
        return False

