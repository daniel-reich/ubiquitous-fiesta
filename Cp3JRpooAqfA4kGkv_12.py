
def node_type(_N, _P, node):
    has_parent = dict(zip(_N, _P)).get(node, -1) != -1
    return {  # (haschildren, hasparent): type
        (True, True): 'Inner',
        (False, True): 'Leaf',
        (True, False): 'Root'
    }.get((node in set(_P), has_parent), 'Not exist')

