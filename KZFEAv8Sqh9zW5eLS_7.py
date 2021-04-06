
def is_val_in_tree(tree, val):
    lst = []
    def helper(tree,val):
        if tree != None:
            if tree[1] != None:
                helper(tree[1],val)
            
            if tree[2] != None:
                helper(tree[2],val)
​
            if tree[0] == val:
                lst.append('found')
​
    
    helper(tree,val)
​
    return 'found' in lst

