
import json
def navigate(roads, start, end):
  rds = json.loads(roads)
  
  V = {v["id"] for v in rds["nodes"]}
  E = {(e["source"],e["target"]):e["metadata"]["distance"] for e in rds["edges"]}
  
  s = sum(E.values())+1
  
  paths = {v:[s,[start,v]] for v in V}
  paths[start] = [0,[start]]
  
  queue = sorted(V, key = lambda v: paths[v][0])
  
  while queue:
    act = queue.pop(0)
    if act == end: return {"path":paths[act][1],"distance":paths[act][0]}
    for v in V:
      if (act,v) in E and paths[act][0] + E[(act,v)] < paths[v][0]:
        paths[v][0] = paths[act][0] + E[(act,v)]
        paths[v][1] = paths[act][1] + [v]
      if (v,act) in E and paths[act][0] + E[(v,act)] < paths[v][0]:
        paths[v][0] = paths[act][0] + E[(v,act)]
        paths[v][1] = paths[act][1] + [v]
    queue = sorted(queue, key = lambda v: paths[v][0])

