
def is_val_in_tree(tree, val):
    for i in range(3):
        if type(tree[i]) == list:
            if is_val_in_tree(tree[i],val):
                return True
        else:
            if tree[i] == val:
                return True
​
    return False

