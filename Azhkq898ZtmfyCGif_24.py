
def numbers_to_ranges(lst):
    r = []
    while len(lst) > 0:
        i = 0
        while len(lst) > 1 and lst[i] + 1 == lst[i + 1]:
            i += 1
            if i + 1 == len(lst):
                break
        if i != 0:    
            add = "{}-{}".format(lst[0], lst[i])
            lst = lst[i + 1 :]
        else:
            add = str(lst[0])
            lst = lst[1:]
        r.append(add)    
    return r

