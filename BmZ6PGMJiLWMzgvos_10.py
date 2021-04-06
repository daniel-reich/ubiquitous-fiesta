
def is_special_array(lst):
    thingy = True
    evens = lst[::2]
    odds = lst[1::2]
    for i in evens:
        if i % 2 != 0:
            thingy = False
    for i in odds:
        if i % 2 == 0:
            thingy = False
    if thingy == False:
        return False
    else:
        return True

