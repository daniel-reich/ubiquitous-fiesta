
def get_path_length(world, width, height):
    homeNode = None
    worldList = loadWorld(world, width, height)
    unvisited = []
    for row in worldList:
        for elem in row:
            unvisited.append(elem)
    
    while len(unvisited) > 0:
        currentNode = minDistance(unvisited)
​
        if currentNode.node_type == 'h':
            homeNode = currentNode
        
        nextNodes = neighbours(worldList, currentNode.coordX, currentNode.coordY)
        
        for elem in nextNodes:
            newDist = currentNode.distance
            newDist = newDist + 1 if elem.node_type != 't' else newDist + 999
            if elem.distance > newDist:
                elem.distance = newDist
        
        unvisited.remove(currentNode)
        
    return -1 if homeNode.distance > 899 else homeNode.distance
  
  
  
def minDistance(unvisited):
    minNode = unvisited[0]
    minDist = unvisited[0].distance
    for node in unvisited:
        if node.distance < minDist:
            minNode = node
            minDist = node.distance    
    return minNode
  
  
  
def neighbours(worldList, coordX, coordY):
    h = len(worldList)
    w = len(worldList[0])
    
    neighbourList = []
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            if coordX + i < w and coordX + i > -1: 
                if coordY + j < h and coordY + j > -1:
                    if i != 0 or j != 0:
                        neighbourList.append(worldList[coordY + j][coordX + i])
    
    return neighbourList
  
  
  
def loadWorld(world, w, h):
    worldList = [[]]
    i = 0
    j = 0
    
    for c in world:
        if c != ',':
            dist = 0 if c == 'm' else 999
            if i == w:
                i = 0
                j += 1
                worldList.append([])
            n = Node(c, dist, i, j)
            i = i + 1
            worldList[j].append(n)
    
    return worldList
  
  
  
class Node:
    
    def __init__ (self, node_type, distance, coordX, coordY):
        self.node_type = node_type
        self.distance = distance
        self.coordX = coordX
        self.coordY = coordY

