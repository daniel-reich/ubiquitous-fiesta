
import json
​
def navigate(roads,start_node,end_node):
  roads = json.loads(roads)
  routes = []
  def find_routes(path=[start_node],dist=0):
    for i in roads["edges"]:
      if i["source"]==path[-1] and i["target"] not in path[:-1]:
        if i["target"]==end_node:
          routes.append([dist+i["metadata"]["distance"],path+[end_node]])
        else:
          find_routes(path+[i["target"]],dist+i["metadata"]["distance"])
      elif i["target"]==path[-1] and i["source"] not in path[:-1]:
        if i["source"]==end_node:
          routes.append([dist+i["metadata"]["distance"],path+[end_node]])
        else:
          find_routes(path+[i["source"]],dist+i["metadata"]["distance"])
  find_routes()
  routes.sort()
  return {"distance": routes[0][0], "path": routes[0][1]}

