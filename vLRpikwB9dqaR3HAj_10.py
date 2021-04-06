
def is_ord_sub(smlst, biglst):
    try:
        lst=[]
        for num in smlst:
            n=biglst.index(num)
            lst.append(n)
            biglst=biglst[n+1:]
    except:
        return False
    else:
        return True

