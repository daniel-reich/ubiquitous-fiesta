
from json import loads
def navigate(roads, startingNode, endingNode):
  roads = loads(roads)
  visited = set()
  graph = dict()
  data = dict()
  for edge in roads["edges"]:
    graph[edge["source"]] = graph.get(edge["source"], []) + [[edge["target"], edge["metadata"]["distance"]]]
    graph[edge["target"]] = graph.get(edge["target"], []) + [[edge["source"], edge["metadata"]["distance"]]]
    if edge["source"] not in data: data[edge["source"]] = {"distance": float("inf"), "previous": None}
    if edge["target"] not in data: data[edge["target"]] = {"distance": float("inf"), "previous": None}
  data[startingNode]["distance"] = 0
​
  nxt = startingNode
​
  while True:
    for i in [j for j in graph[nxt] if j[0] not in visited]:
      if data[i[0]]["distance"] > data[nxt]["distance"] + i[1]:
        data[i[0]]["distance"] = data[nxt]["distance"] + i[1]
        data[i[0]]["previous"] = nxt
    visited.add(nxt)
    nxt = sorted([k for k in data if k not in visited], key=lambda x: data[x]["distance"])
    if not nxt: break
    nxt = nxt[0]
    
  path = [endingNode]
  
  while True:
    if data[path[-1]]["previous"] is not None:
      path.append(data[path[-1]]["previous"])
    else:
      break
  
  return {'distance': data[endingNode]["distance"], 'path': path[::-1]}

