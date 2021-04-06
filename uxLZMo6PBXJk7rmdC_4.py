
class Path_Object():
  def __init__(self):
    self.paths=[]
    self.dists=[]
def path_finder(start,end,path,distance,edges,p_obj):
    path=path[:]
    path.append(start)
    #print(path,distance)
    if start==end:
        p_obj.paths.append(path)
        p_obj.dists.append(distance)
        
    for e in edges[start]:
        if not e in path:
            new_dist=distance+edges[start][e]
            path_finder(e,end,path,new_dist,edges,p_obj)
​
def navigate(roads, startingNode, endingNode):
  import json
  roads=json.loads(roads)
  nodes=[r["id"] for r in roads["nodes"]]
  road_d={n:{} for n in nodes}
  for e in roads["edges"]:
    dist=e["metadata"]["distance"]
    n1=e["target"]
    n2=e["source"]
    #print(n1,n2,dist)
    road_d[n1][n2]=dist
    road_d[n2][n1]=dist
  p_obj=Path_Object()
  path_finder(startingNode,endingNode,[],0,road_d,p_obj)
  min_i=p_obj.dists.index(min(p_obj.dists))
  result={"path":p_obj.paths[min_i],"distance":p_obj.dists[min_i]}
  return result

