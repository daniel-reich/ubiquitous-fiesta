
def is_val_in_tree(tree, val):
    for x in tree:
        if isinstance(x, list):
            if is_val_in_tree(x, val):
                return True
        if x == val:
            return True
    return False

