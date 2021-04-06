
import json, heapq, collections
def dijkstra(g, source):
  dist = collections.defaultdict(lambda: (float('inf'), []))
  pq = []
  heapq.heappush(pq, (0, [source]))
  while pq:
    d, path = heapq.heappop(pq)
    v = path[-1]
    if d >= dist[v][0]: continue
    dist[v] = d, path
    for u, w in g[v]:
      heapq.heappush(pq, (d+w, path + [u]))
  return dist
def navigate(roads, startingNode, endingNode):
  roads = json.loads(roads)
  g = {v['id']: [] for v in roads['nodes']}
  for e in roads['edges']:
    g[e['source']].append((e['target'], e['metadata']['distance']))
    g[e['target']].append((e['source'], e['metadata']['distance']))
  distance, path = dijkstra(g, startingNode)[endingNode]
  return {'distance': distance, 'path': path}

