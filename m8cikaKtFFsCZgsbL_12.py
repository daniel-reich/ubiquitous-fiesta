
from heapq import heappop, heappush
from itertools import combinations
​
def pours(curr, avail):
    for a, b in combinations(range(len(avail)), 2):
        # pour from a to b and b to a
        for x, y in [(a, b), (b, a)]:
            if curr[x] < avail[x] and curr[y] > 0:
                new = list(curr)
                to_give = min(avail[x]-curr[x], curr[y])
                new[x] += to_give
                new[y] -= to_give
                yield tuple(new)
​
def waterjug(start, goal):
  state = [0 for _ in start]
  state[-1] = start[-1]
  
  Q = []
  dists = {tuple(state): 0,}
  heappush(Q, (0, tuple(state)))
​
  while Q:
      d, u = heappop(Q)
      if u == tuple(goal):
          return d
      for v in pours(u, start):
          d2 = d + 1
          if tuple(v) in dists:
              continue
          dists[v] = d2
          heappush(Q, (d2, v))
  return 'No solution.'

