
from collections import deque
def jumping_frog(n, stones):
  exits = [i for i in range(n) if i + stones[i] >= n]
  distances = {i : 1 for i in exits}
  q =  deque(exits)
  while q and 0 not in distances:
    cur = q.popleft()
    neighbors = [i for i in range(n) if i not in distances and(
                                      i + stones[i] == cur or 
                                       i - stones[i] == cur)]
    for nbr in neighbors:
      distances[nbr] = distances[cur] + 1
      q.append(nbr)
  return distances[0] + 1 if 0 in distances else 'no chance :-('

