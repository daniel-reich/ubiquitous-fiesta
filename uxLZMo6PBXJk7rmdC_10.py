
import json
def navigate(roads, startingNode, endingNode):
  graph = json.loads(roads)
  nodes = [node["id"] for node in graph["nodes"]]
  edges = {node: [] for node in nodes}
  for edge in graph["edges"]:
    edges[edge["source"]].append(edge)
    edges[edge["target"]].append(edge)
  dist = {}
  prev = {}
  Q = set()
  for node in nodes:
    dist[node] = 10000
    prev[node] = None
    Q.add(node)
  dist[startingNode] = 0
  while Q:
    u = min(Q, key=lambda n: dist[n])
    Q.discard(u)
    if u == endingNode:
      break
    for edge in edges[u]:
      v = edge["target"] if edge["source"] == u else edge["source"]
      alt = dist[u] + edge["metadata"]["distance"]
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u
  path = []
  u = endingNode
  while u is not None:
    path = [u] + path
    u = prev[u]
  path_dist = [
    [e for e in edges[s] if t in (e["target"], e["source"])]
    for s, t in zip(path[:-1], path[1:])
  ]
  return {
    "path": path,
    "distance": sum(d[0]["metadata"]["distance"] for d in path_dist),
  }

