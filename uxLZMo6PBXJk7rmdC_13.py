
import json
roads = """
{
  "directed": false,
  "nodes": [
    { "id": 0 },
    { "id": 1 },
    { "id": 2 },
    { "id": 3 },
    { "id": 4 },
    { "id": 5 },
    { "id": 6 },
    { "id": 7 },
    { "id": 8 },
    { "id": 9 }
  ],
  "edges": [
    {
      "source": 1,
      "target": 6,
      "label": "Oak Street",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 6,
      "target": 8,
      "label": "Oak Street",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 8,
      "target": 9,
      "label": "Oak Street",
      "metadata": {
        "distance": 11
      }
    },
    {
      "source": 8,
      "target": 7,
      "label": "Robin Way",
      "metadata": {
        "distance": 3
      }
    },
    {
      "source": 7,
      "target": 4,
      "label": "Robin Way",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 6,
      "target": 7,
      "label": "Mountain Road",
      "metadata": {
        "distance": 8
      }
    },
    {
      "source": 7,
      "target": 9,
      "label": "Mountain Road",
      "metadata": {
        "distance": 9
      }
    },
    {
      "source": 4,
      "target": 3,
      "label": "National Street",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 1,
      "target": 0,
      "label": "Sunrise Drive",
      "metadata": {
        "distance": 4
      }
    },
    {
      "source": 0,
      "target": 3,
      "label": "Short Street",
      "metadata": {
        "distance": 3
      }
    },
    {
      "source": 5,
      "target": 4,
      "label": "Rickety Creek",
      "metadata": {
        "distance": 7
      }
    },
    {
      "source": 4,
      "target": 0,
      "label": "Rickety Creek",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 9,
      "target": 5,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 5,
      "target": 2,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 2,
      "target": 3,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 7
      }
    }
  ]
}
"""
#-----------------------------------------------------------------------
def getDistance(mp, p1, p2):
    #print("\n\nDistances")
    for x in mp['edges']:
        #print('S {} T {} D {}'.format(x['source'], x['target'], x['metadata']['distance']))
        if(x['source'] == p1 and x['target'] == p2):
            return x['metadata']['distance']
        elif(x['target'] == p1 and x['source'] == p2):
            return x['metadata']['distance']
    else:
        return 9999
​
#-----------------------------------------------------------------------
def getNodes(mp):
    lst = []
    for x in mp['nodes']:
        lst.append(x['id'])
    return lst
​
#-----------------------------------------------------------------------
def getUnvisitedNeighbors(mp, visiting, notVisited, table):
    res = []
    nwMp = mp['edges']
    for node in notVisited:
        for mpEnt in nwMp:
            # node not same as 'visiting node' and node connected to visiting
            if(visiting != node and
               ((mpEnt['source'] == node) and
                (mpEnt['target'] == visiting)) or
               ((mpEnt['target'] == node) and
                (mpEnt['source'] == visiting))):
​
                # Add [node, distace to start] to list
                distStartToNode = getDistance(mp, node, visiting)
                distStartToNode += table[visiting][1]
                res.append([node, distStartToNode])
    res.sort(key= lambda v: v[1])
    return res
​
#-----------------------------------------------------------------------
# Get next node to visit
# Table[[a, b, c],...]
#   a = node index
#   b = distance to start node
#   c = previous node
def getNextNode(table, notVisited):
    nd = -1
    min = 1000000
    for entry in table:
        if(entry[0] in notVisited and entry[1] < min):
            nd = entry[0]
            min = entry[1]
    return nd
    
​
​
def navigate(roads, start, end):
    mp = json.loads(roads)
    #print(mp)
    d = getDistance(mp, 0, 3)
​
    # Initialize data
    nds = getNodes(mp)    
    visited = []
    notVisited = nds[:]
​
    # Initialize table
    table = []
    for n in nds:
        table.append([n, 1000, 1000])
    table[start][1] = 0
    table[start][2] = start
    #print('TABLE {}'.format(table))
​
​
    while(len(notVisited) > 0):
        #print('\nTABLE {} NOT VIS {}'.format(table, notVisited))
        visiting = getNextNode(table, notVisited)
        #print('Vistiting {}'.format(visiting))
        vals = getUnvisitedNeighbors(mp, visiting, notVisited, table)
        #print('LIST {}'.format(vals))
        for v in vals:
            ind = v[0]
            if(v[1] < table[ind][1]):
                table[ind][1] = v[1]
                table[ind][2] = visiting
        indxNd = notVisited.index(visiting)
        visited.append(notVisited.pop(indxNd))
​
    nd = end
    path = []
    path.append(nd)
    while nd != start:
        n = table[nd][2]
        path.append(n)
        nd = n
    path.reverse()
    #print(path)
    ret = {'distance': table[end][1], 'path':path}
    return ret

