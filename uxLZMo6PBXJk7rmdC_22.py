
import json
from collections import namedtuple
​
Edge = namedtuple('Edge', 'target distance')
Node = namedtuple('Node', 'distance route visited')
​
# Could improve with a heap.
def lowest_unvisited(nodes):
  lowest = None
  lowest_id = -1
  for id, node in nodes.items():
    if not node.visited and node.distance is not None:
      if lowest is None or lowest.distance > node.distance:
        lowest = node
        lowest_id = id
  return lowest_id, lowest
​
def navigate(roads, startingNode, endingNode):
  graph = json.loads(roads)
  edges = {}
  nodes = {}
  for node in graph['nodes']:
    edges[node['id']] = set()
    nodes[node['id']] = Node(None, [], False)
  for edge in graph['edges']:
    edges[edge['source']].add(Edge(edge['target'], edge['metadata']['distance']))
    edges[edge['target']].add(Edge(edge['source'], edge['metadata']['distance']))
  nodes[startingNode] = Node(0, [startingNode], False)
  while not nodes[endingNode].visited:
    id, node = lowest_unvisited(nodes)
    nodes[id] = Node(node.distance, node.route, True)
    for edge in edges[id]:
      other = nodes[edge.target]
      if not other.visited:
        new_distance = node.distance + edge.distance
        if other.distance is None or other.distance > new_distance:
          nodes[edge.target] = Node(new_distance, node.route + [edge.target], False)
  return {"distance": nodes[endingNode].distance,
          "path": nodes[endingNode].route }

