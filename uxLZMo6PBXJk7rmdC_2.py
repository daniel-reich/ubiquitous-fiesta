
import json, heapq
from collections import defaultdict
​
def navigate(roads, start, end):
    d = json.loads(roads)    
    graph = defaultdict(dict)
    
    for i in d['edges']:
        graph[i['source']].update({i['target']: i['metadata']['distance']})
        graph[i['target']].update({i['source']: i['metadata']['distance']})
​
    visited = set()
    stack = [(0, start, [])]
    
    while True:
        distance, node, path = heapq.heappop(stack)
        if node not in visited:
            path = path + [node]
            visited.add(node)
            if node == end:
                return {'distance': distance, 'path': path}
            for (next_node, i) in graph[node].items():
                heapq.heappush(stack, (distance + i, next_node, path))

