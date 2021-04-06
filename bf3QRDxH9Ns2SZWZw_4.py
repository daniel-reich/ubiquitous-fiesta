
from collections import defaultdict, deque
​
def matrix(grid): 
  adjacents = defaultdict(lambda: "0")
  matrice = defaultdict(lambda: "0")
  shifts = {"+": [(1,0),(-1,0),(0,1),(0,-1)],
            "x": [(1,1),(1,-1),(-1,1),(-1,-1)]}
  num = 0
  for i, line in enumerate(grid):
    for j, char in enumerate(line):
        matrice[(i,j)]= char
        if char != "0":
          num += 1
          adjacents[(i,j)] = [(i+shift[0],j+shift[1]) 
                              for shift in shifts[char]
                              ]
  print (num)
  return adjacents, matrice, num
​
def bfs(graph, root, matrice): 
  visited, queue = set(), deque([root])
  while queue: 
    vertex = queue.popleft()
    for neighbour in graph[vertex]:
      if neighbour not in visited and matrice[neighbour] != "0": 
        visited.add(neighbour) 
        queue.append(neighbour)
  print (len(visited))
  return visited
  
def all_explode(grid):
  adjacents, matrice, num = matrix(grid)
  if len(bfs(adjacents,(0,0), matrice)) == num:
    return True
  else:
    return False

