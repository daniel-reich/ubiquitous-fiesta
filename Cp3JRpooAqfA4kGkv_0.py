
def node_type(nodes, parents, value):
    if value not in nodes:
        return 'Not exist'
    if parents[nodes.index(value)] == -1:
        return 'Root'
    if value not in parents:
        return 'Leaf'
    return 'Inner'

