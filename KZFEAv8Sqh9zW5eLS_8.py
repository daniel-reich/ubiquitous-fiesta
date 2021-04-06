
def is_val_in_tree(lst, val):
    if lst:
        if lst[0] == val:
            return True
        elif is_val_in_tree(lst[1], val):
            return True
        elif is_val_in_tree(lst[2], val):
            return True
    return False

