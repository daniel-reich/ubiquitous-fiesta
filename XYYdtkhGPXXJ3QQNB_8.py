
def num_in_str(lst):
    s = []
    for x in lst:
        for y in x:
            if y in '0123456789':
                s.append(x)
                break
    return s

