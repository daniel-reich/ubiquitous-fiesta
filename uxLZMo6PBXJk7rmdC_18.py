
from heapq import heappush, heappop
import json
​
def navigate(roads, startingNode, endingNode):  
  graph = json.loads(roads)
  nodes = {node["id"]: {} for node in graph["nodes"]}
  weights = {id: float("inf") for id in nodes.keys()}
  for edge in graph["edges"]:
    node1 = edge["source"]
    node2 = edge["target"]
    distance = edge["metadata"]["distance"]
    nodes[node1].update({node2: distance})
    nodes[node2].update({node1: distance})
  min_heap = []
  visited = set()
  weights[startingNode] = 0
  heappush(min_heap, (0, startingNode))
  while len(min_heap):
    weight, node = heappop(min_heap)
    if node in visited:
      continue
    visited.add(node)
    for neighbor, distance in nodes[node].items():
      new_distance = min(weight + distance, weights[neighbor])
      weights[neighbor] = new_distance
      heappush(min_heap, (new_distance, neighbor))
  result = {"path": [],
            "distance": weights[endingNode]}
  node = endingNode
  result["path"].insert(0, node)
  while node != startingNode:
    node = min([(weights[neighbor], neighbor) for neighbor in nodes[node]], key=lambda n: n[0])[1]
    result["path"].insert(0, node)
  return result

