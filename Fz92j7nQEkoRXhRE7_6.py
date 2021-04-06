
def jumping_frog(n, stones):
  que = [(0, 1)]
  visited = {0}
  while len(que) > 0:
    pos, steps = que.pop(0)
    lpos = pos - stones[pos]
    rpos = pos + stones[pos]
    if rpos >= n:
      return steps + 1
    if lpos >= 0 and lpos not in visited:
      que.append((lpos, steps + 1))
      visited.add(lpos)
    if rpos < n and rpos not in visited:
      que.append((rpos, steps + 1))
      visited.add(rpos)
  return 'no chance :-('

