
def largest_island(lst):
  m = 0
  visited = set()
  nb = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
  
  for i, r in enumerate(lst):
    for j, c in enumerate(r):
      if c and (i, j) not in visited:
        length = 1
        visited.add((i, j))
        stack = [(i, j)]
        
        while stack:
          cr, cc = stack.pop()
          
          for y, x in [(cr+nr, cc+nc) for nr, nc in nb if 0<=cr+nr<len(lst) and 0<=cc+nc<len(lst[0])]:
            if lst[y][x] and (y, x) not in visited:
              visited.add((y, x))
              length += 1
              stack.append((y, x))
              
        m = max((m, length))
  return m

