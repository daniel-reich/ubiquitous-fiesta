
from heapq import heapify, heappop, heappush
import json
​
def moves(G, curr):
    for edge in G['edges']:
        if edge['source'] == curr:
            yield edge['target'], edge['metadata']['distance']
        elif edge['target'] == curr:
            yield edge['source'], edge['metadata']['distance'] 
​
def navigate(roads, starting_node, ending_node):
  G = json.loads(roads)
  Q = []
  dists = {starting_node: 0,}
  prev = {starting_node: None}
  heappush(Q, (0, starting_node))
​
  while Q:
      d, u = heappop(Q)
      if u == ending_node:
          break
      for v, x in moves(G, u):
          d2 = d + x
          if v in dists and dists[v] <= d2:
              continue
          dists[v] = d2
          prev[v] = u
          heappush(Q, (d2, v))
​
  n = ending_node
  path = [n,]
  while prev[n] is not None:
      path.append(prev[n])
      n = path[-1]
  return {'distance': dists[ending_node], 'path':path[::-1]}

