
def last_ancestor(tree, f1, f2):
    '''
    Returns the nearest common ancestor of f1 and f2 in tree, where tree
    is a dictionary of folders to sub-folders as per instructions
    '''
    parents = {c: p for p in tree for c in tree[p]} # children tree
    root = [c for c in tree if c not in parents][0] # root of tree
    parents.update({root:None})
    path = lambda x: [] if not x else [x] + path(parents[x])
​
    p1 = path(f1)
    p2 = path(f2)  # family trees of f1 and f2
    
    return [f for f in p1 if f in p2][0]  # 1st common ancestor

