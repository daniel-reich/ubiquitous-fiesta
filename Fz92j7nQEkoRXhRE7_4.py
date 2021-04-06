
def jumping_frog(n, stones):
  current = 0
  steps = 1
  while current + stones[current] < len(stones):
    left = current - stones[current]
    right = current + stones[current]
    try:
      if stones[left] + left > len(stones):
        return steps + 2
    except IndexError:
      pass
    if stones[right] == 0:
      return "no chance :-("
    current += stones[current]
    steps += 1
  return steps + 1

