
def validate_swaps(lst, txt):
    booleans = []
    for i in lst:
        if set(i) != set(txt):
            booleans.append(False)
        else:
            count = 0
            for g,c in zip(i,txt):
                if g != c:
                    count = count + 1
            if count > 2:
                booleans.append(False)
            else:
                booleans.append(True)
    return booleans

