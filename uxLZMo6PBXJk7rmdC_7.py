
import json
import heapq
​
class UndirectedGraph():
​
    def __init__(self):
        self.nodes = []
        self.edges = {}
​
    def AddNode(self, node):
        # add node; do nothing if node already exists
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.edges[node] = {}
​
    def AddEdge(self, node1, node2, weight=1):
        # add edge (optionally with weight)
        assert node1 in self.nodes and node2 in self.nodes
        if node1 not in self.edges[node2]:
            self.edges[node2][node1] = weight
        if node2 not in self.edges[node1]:
            self.edges[node1][node2] = weight
​
    def GetNodes(self):
        return self.nodes
​
    def GetEdges(self, node):
        return self.edges.get(node, {})
​
    def GetWeightedEdges(self, node):
        return self.edges[node].items()
​
    def GetDegree(self, node):
        return len(self.edges.get(node, {}).keys())
​
    def Dijkstra(self, s, t):
        BIGNUM = 2**31
        X = set()
        key = {node: BIGNUM for node in self.GetNodes()}
        key[s] = 0
        H = [(v, k) for k, v in key.items()]
        Len = {s: 0}
        heapq.heapify(H)
        prev = {node: None for node in self.GetNodes()}
        while len(H) > 0:
            key_wstar, wstar = heapq.heappop(H)
            X.add(wstar)
            Len[wstar] = key[wstar]
            for y, weight in self.GetWeightedEdges(wstar):
                if prev[y] == None:
                    prev[y] = wstar
                if (key[y], y) in H:
                    H.remove((key[y], y))
                    if Len[wstar] + weight < key[y]:
                        key[y] = Len[wstar] + weight
                        prev[y] = wstar
                    key[y] = min(key[y], Len[wstar] + weight)
                    if y not in X:
                        heapq.heappush(H, (key[y], y))
            heapq.heapify(H)
        path = [t]
        cur = t
        while cur != s:
            cur = prev[cur]
            path.append(cur)
        ans = {"distance": Len[t], "path": path[::-1]}
        return ans
     
        
        
def navigate(roads, startingNode, endingNode):
    data = json.loads(roads)
    G = UndirectedGraph()
    for item in data['nodes']:
        G.AddNode(item['id'])
    for item in data['edges']:
        node1 = item['source']
        node2 = item['target']
        distance = item['metadata']['distance']
        G.AddEdge(node1, node2, distance)
        G.AddEdge(node2, node1, distance)
    return G.Dijkstra(startingNode, endingNode)

