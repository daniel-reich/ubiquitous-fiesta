
def is_val_in_tree(tree, val):
    is_val=False
    if not isinstance(tree,list):
        if tree == val:
            return True
        else:
            return False
    
    for l in tree:
        
        is_val =is_val_in_tree(l,val)
        if is_val:
            break
        
    return is_val

