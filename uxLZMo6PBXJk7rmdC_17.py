
def get_graph(j_graph):
    '''
    Generates a graph suitable for the problem from the json j_graph.
    '''
    import json
​
    g = json.loads(j_graph)
    nodes = sorted([item['id'] for item in g['nodes']])
    edges = [(item['source'],item['target'],item['metadata']['distance']) \
             for item in g['edges']]  # node, node, weight(distance)
    edges = sorted(edges + [(b,a,w) for a,b,w in edges]) # add reverse links & sort
    
    return {node:[(b,w) for a,b,w in edges if a == node] for node in nodes} # link them
    
​
def navigate(roads, s, e):
    '''
    Returns the shortest distance and path between nodes s and e as per instructions.
    roads is a JSON style graph. Uses Dijkstra's algorithm with priority queue.
    '''
    import heapq as h
    
    graph = get_graph(roads)  # convert to more usable format
    distances = {node: float('inf') for node in graph}
    prev = {node: -1 for node in graph}  # to trace the path
    q = []
    distances[s] = 0
    h.heappush(q, (0, s))  # start node in the queue at distance 0
​
    while q:
        u = h.heappop(q)[1]
        if u == e:
            break  # reached target node
        
        for edge, dis in graph[u]:
            if distances[edge] > distances[u] + dis:
                distances[edge] = distances[u] + dis
                prev[edge] = u
                h.heappush(q, (distances[edge], edge))  # queue at distance priority
​
    distance = distances[e]
    path = []
    node = e
    while node != -1:
        path.append(node)
        node = prev[node]
​
    return {'distance': distance, 'path': path[::-1]}

