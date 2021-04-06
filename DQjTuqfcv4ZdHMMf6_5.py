
def kaprekar(num):
    iiii = 0
    while num != 6174:
        x = str(num)
        lst, tsl = [], []
        for y in x:
            lst.append(y)
        lst = sorted(lst)
        l = len(lst)
        i = 0
        while l != i:
            tsl.append(lst[l-1])
            l = l - 1
        lst1 = ""
        tsl1 = ""
        for x in lst:
            lst1 = lst1 + str(x)
        for x in tsl:
            tsl1 = tsl1 + str(x)
        lst = int(lst1)
        tsl = int(tsl1)
        num = abs(lst - tsl)
        if num < 1000:
            num = num*10
        iiii = iiii + 1
    return iiii
kaprekar(1112)

