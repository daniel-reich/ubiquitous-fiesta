
from itertools import permutations
from collections import deque
​
​
def step(tpl):
    lc = [(tpl[0]+x, tpl[1]+y) for x, y in permutations([1, 2, -1, -2], 2)
          if abs(x) != abs(y)]
    return [(i, j) for i, j in lc if 1 <= i <= 8 and 1 <= j <= 8]
​
​
def knight_bfs(a, b, c, d):
    queue = deque([[(a, b)]])
    discovered = set([])
    while queue:
        next = queue.popleft()
        node = next[-1]
        if node not in discovered:
            discovered.add(node)
            links = step(node)
            for link in links:
                way = list(next)
                way.append(link)
                queue.append(way)
                if link == (c, d):
                    return len(way) - 1
    return False

