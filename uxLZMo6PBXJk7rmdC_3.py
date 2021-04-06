
import json
​
class Node(object):
​
    def __init__(self, id, edges):
        self.id = id
        self.connected_nodes = {}
        for e in edges:
            if e['source'] == self.id:
                self.connected_nodes[e['target']] = e['metadata']['distance']
            elif e['target'] == self.id:
                self.connected_nodes[e['source']] = e['metadata']['distance']
​
def newResult(baseResult=None, nextNode=None, dist=None):
    if baseResult is None:
        result = {'distance': 0, 'path': [nextNode]}
    else:
        result = {}
        result['distance'] = baseResult['distance']
        result['path'] = baseResult['path'][:]
    if dist is not None:
        result['distance'] = result['distance'] + dist
        result['path'].append(nextNode)
    return result
​
def recurseNodes(nodes, startingNode, endingNode, baseResult=None):
    baseResult = newResult(baseResult, startingNode)
    resultDict = {}
    baseNode = nodes[startingNode]
    isDeadEnd = True
    for key, value in baseNode.connected_nodes.items():
        if key not in baseResult['path']:
            isDeadEnd = False
            resultDict[key] = newResult(baseResult, key, value)
            if key != endingNode:
                resultDict[key] = recurseNodes(nodes, key, endingNode, resultDict[key])
    if isDeadEnd:
        return None
    else:
        shortestDist = -1
        for k2, v2 in resultDict.items():
            if v2 is not None:
                if shortestDist == -1 or v2['distance'] < shortestDist:
                    shortestDist = v2['distance']
                    shortestKey = k2
        if shortestDist == -1:
            return None
        else:
            return resultDict[shortestKey]
​
def navigate(roads, startingNode, endingNode):
    nodes = {}
    d = json.loads(roads)
    for n in d['nodes']:
        newNode = Node(n['id'],d['edges'])
        nodes[newNode.id] = newNode
    result = recurseNodes(nodes, startingNode, endingNode)
    return result

