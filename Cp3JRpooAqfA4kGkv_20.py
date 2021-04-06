
def node_type(nodes, parents, n):
    if n not in nodes:
        return 'Not exist'
    parent = parents[nodes.index(n)]
    if parent not in nodes:
        return 'Root'
    if n in parents:
        return 'Inner'
    return 'Leaf'

