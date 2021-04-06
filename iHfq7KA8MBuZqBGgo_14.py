
def is_legitimate(lst):
    touch_lr = all([sublist[0]==0 and sublist[-1]==0 for sublist in lst])
    touch_ud = 1 not in lst[0] and 1 not in lst[-1]
    return touch_lr and touch_ud

