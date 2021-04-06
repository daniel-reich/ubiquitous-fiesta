
from collections import defaultdict
import math
​
class UndirectedGraph():
    
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
​
    def dijsktra(self, initial, end):
        graph = self
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()
        
        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]
​
            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
            
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        
        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path
​
graph = UndirectedGraph()
​
diags = []
for r in range(1, 5):
    x1, y1 = r, 0
    a = r / math.sqrt(2)
    x2, y2 = a, a
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    diags.append(dist)
seq = "ABCDEFGH"
edges = []
for k in range(8):
    edges.append(("A0", chr(65 + k) + "1", 1))
for ring in range(1, 4):
    for k in range(8):
        edges.append((seq[k]+str(ring), seq[k]+str(ring+1), 1))
for ring in range(1, 5):
    for k in range(8):
        edges.append((seq[k]+str(ring), seq[(k+1)%8]+str(ring), diags[ring-1]))
for edge in edges:
    graph.add_edge(*edge)
​
def spider_vs_fly(spider, fly):
    return '-'.join(graph.dijsktra(spider, fly))

