
import json
​
class Vertex:
  def __init__(self, key):
    self.id = key 
    self.connectedTo = {}
​
  def addNeighbor(self, nbr, weight=0):
    self.connectedTo[nbr] = weight
​
  def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
​
  def getConnections(self):
    return self.connectedTo.keys()
​
  def getId(self):
    return self.id
​
  def getWeight(self, nbr):
    return self.connectedTo[nbr]
​
class Graph:
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0 
​
  def addVertex(self, key):
    self.numVertices = self.numVertices + 1 
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex
    
  def getVertex(self, n): 
    if n in self.vertList:
      return self.vertList[n]
    else:
      return None
​
  def addEdge(self, f, t, cost=0):
    if f not in self.vertList:
      nv = self.addVertex(f)
    if t not in self.vertList:
      nv = self.addVertex(t)
    self.vertList[f].addNeighbor(self.vertList[t], cost)
    self.vertList[t].addNeighbor(self.vertList[f], cost)
​
  def getVertices(self):
    return self.vertList.keys()
​
  def __iter__(self):
    return iter(self.vertList.values())
​
​
​
def navigate(roads, startingNode, endingNode):
  data = json.loads(roads)
  n = len(data['nodes'])
  visited = [False for i in range(n)]
  edges = data['edges']
  g = Graph()
  for edge in edges:
    g.addEdge(edge['source'], edge['target'], edge['metadata']['distance'])
    
  start = g.getVertex(startingNode)
  end = g.getVertex(endingNode)
  frontier = [(0,start)]
  queue = list() 
  came_from = {}
  came_from[start] = None
  return_dict = {}
  while frontier: 
    queue += frontier
    current = queue.pop(0)[1]
    if visited[current.getId()]:
      continue
    if current == end:
      return_dict['distance'] = 0
      return_dict['path'] = []
      node_source = current
            
      while node_source is not None:
        prev_node = came_from[node_source]
        if prev_node is None:
          return_dict['path'].insert(0, node_source.getId())
          return return_dict
​
        return_dict['distance'] +=  node_source.getWeight(prev_node)
        return_dict['path'].insert(0, node_source.getId())
        node_source = prev_node
​
    for vert in current.getConnections():
      if vert not in came_from.keys():
        came_from[vert] = current
      frontier.append((vert.getWeight(current), vert))
    visited[current.getId()] = True
    frontier.sort(key=lambda x: x[0])

