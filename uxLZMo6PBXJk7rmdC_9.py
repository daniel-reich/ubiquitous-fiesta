
# How this works
# 1. Build graph with id and all paths
​
​
import json
from heapq import heappush, heappop
from collections import defaultdict
​
​
def dijkstra(graph, source):
    all_pathes = []
    dist_dict = defaultdict(lambda: (float('inf'), []))
    heappush(all_pathes, (0, [source]))
    while all_pathes:
        dist, path = heappop(all_pathes)
        v = path[-1]
        if dist >= dist_dict[v][0]:
            continue
        dist_dict[v] = dist, path
        for curr_path, curr_distance in graph[v]:
            heappush(all_pathes, (dist + curr_distance, path + [curr_path]))
    return dist_dict
​
​
def navigate(roads, startingNode, endingNode):
    roads = json.loads(roads)
    graph = {v['id']: [] for v in roads['nodes']}
    for edge in roads['edges']:
        graph[edge['source']].append((edge['target'], edge['metadata']['distance']))
        graph[edge['target']].append((edge['source'], edge['metadata']['distance']))
    distance, path = dijkstra(graph, startingNode)[endingNode]
    return {'distance': distance, 'path': path}

