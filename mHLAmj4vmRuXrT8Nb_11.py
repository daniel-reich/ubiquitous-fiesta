
def consecutive_combo(lst1, lst2):
    new_list = sorted(lst1 + lst2)
    return True if sum(new_list) == sum(range(new_list[0], new_list[-1] + 1)) else False

