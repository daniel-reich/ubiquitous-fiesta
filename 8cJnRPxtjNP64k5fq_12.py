
def dance(lst, parameter):
    m = list(map(lambda x:x[1],lst))
    wm = list(map(lambda x:x[0],lst))
    if parameter=='men':
        m = m[::-1]
        return list(map(lambda x:list(x),list(zip(wm,m))))
    else:
        wm=wm[::-1]
        return list(map(lambda x:list(x),list(zip(wm,m))))

