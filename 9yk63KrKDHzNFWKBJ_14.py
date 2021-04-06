
def is_it_inside(graph, end, start):
  stack = [start]
  visited = [start]
  
  while stack:
    node = stack.pop()
    
    if node == end:
      return True
    
    if node not in graph:
      continue
    
    for neighbors in graph[node]:
      if neighbors not in visited:
        stack.append(neighbors)
        visited.append(neighbors)
  
  return False

