
def node_type(kids, parents, node):
    '''
    Returns the type of node that node is, based on the instructions
    '''
    if node in parents:
        pos = kids.index(node)
        if parents[pos] == -1:
            return 'Root'
        return 'Inner'
​
    if node not in kids:
        return 'Not exist'
    return 'Leaf'

