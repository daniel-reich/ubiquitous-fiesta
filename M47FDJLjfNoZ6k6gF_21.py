
def cup_swapping(lst):
    c_l = 'B'
    for item in lst:
        if c_l in item:
            c_l = item.replace(c_l,'')
    return c_l

