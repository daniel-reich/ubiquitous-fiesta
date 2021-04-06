
import json
def navigate(roads, startingNode, end):
    roads = json.loads(roads)
    edges = {node['id']: set() for node in roads['nodes']}
    for edge in roads['edges']:
        edges[edge['source']].add((edge['target'], edge['metadata']['distance']))
        edges[edge['target']].add((edge['source'], edge['metadata']['distance']))
    shortest_to, depleted =  {startingNode: {'path': [startingNode], 'distance': 0}}, set()
    def is_better(node):
        return adjacent in shortest_to and adjacent not in depleted and\
                shortest_to[adjacent]['distance'] > shortest_to[node]['distance']+dist
    while len(depleted)<len(edges):
        current_level = [(node, p_d['path'], p_d['distance']) for node, p_d in shortest_to.items()]
        for node, path, dist in current_level:
            adjacents = edges[node]
            for adjacent,dist in adjacents:
                if is_better(adjacent) or adjacent not in shortest_to:
                    shortest_to[adjacent] = {'path':path+[adjacent], 'distance':shortest_to[node]['distance']+dist}
            depleted.add(node)
    return shortest_to[end]

