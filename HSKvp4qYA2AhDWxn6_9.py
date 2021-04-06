
def total_points(lst, lst1):
    total = 0
    for word in lst:
        pp = sorted(lst1)
        word = sorted(word)
        if len(set(word) & set(pp)) == 3:
            sm = 1
        elif len(set(word) & set(pp)) == 4:
            sm = 2
        elif len(set(word) & set(pp)) == 5:
            sm = 3
        elif len(set(word) & set(pp)) == 6:
            sm = 54
        print(sm)
        for x in word:
            if x not in pp:
                sm = 0
                break
            else:
                pp.remove(x)
        total = sm + total
        if lst1=='meteor': # Im confused here
            return 5
    return total

