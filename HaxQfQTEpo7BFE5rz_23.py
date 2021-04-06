
def alternate_pos_neg(lst):
    for i in lst:
        if i == 0:
            return False
    for i in range(len(lst) - 1):
        if lst[i] > 0 and lst[i+1] < 0 or lst[i] < 0 and lst[i+1] >0:
            pass
        else:
            return False
    return True

