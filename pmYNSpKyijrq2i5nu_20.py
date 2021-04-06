
def darts_solver(s, darts, target):
  solution = set()
  if darts == 4:
    for a in range(len(s)):
      for b in range(len(s)):
        for c in range(len(s)):
          for d in range(len(s)):
            if sum([s[a], s[b], s[c], s[d]]) == target:
              solution.add(tuple(sorted(((s[a], s[b], s[c], s[d])))))
  else:
    for a in range(len(s)):
      for b in range(len(s)):
        for c in range(len(s)):
          if sum([s[a], s[b], s[c]]) == target:
            solution.add(tuple(sorted((s[a], s[b], s[c]))))
​
  a = sorted(solution, key=lambda x: (x[0], x[1]))
  return ['-'.join(map(str, x)) for x in a]

