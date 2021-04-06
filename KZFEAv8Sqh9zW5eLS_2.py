
def is_val_in_tree(tree, val):
    for i in tree:
        if i == val or isinstance(i, list) and is_val_in_tree(i, val):
            return True
    return False

