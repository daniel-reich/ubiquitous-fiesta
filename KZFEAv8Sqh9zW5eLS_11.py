
def fly(item):
    try:
        for i in iter(item):
            for j in fly(i):
                yield j
    except TypeError:
        yield item
        
def is_val_in_tree(tree, val):
​
    res = [ i for i in fly(tree)]
​
    for i in res:
        if i == val:
            return True
    return False

