
def tf_lst(lst):
    if sum(lst) == 0:
        return False
    if lst[2] + lst[4] != lst[5]:
        return False
    if lst[4]**2 != lst[6]:
        return False
    if lst[1] / 2 != lst[4]:
        return False
    if lst[3] / 267.5 != lst[7]:
        return False
    if lst[0] != lst[4]/10+10:
        return False
    return True

