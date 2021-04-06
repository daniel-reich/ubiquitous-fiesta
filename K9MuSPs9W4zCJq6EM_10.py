
def cycle_length(lst, n):
  s = sorted(lst)
  steps = 0
  fixed = False
  lastused = n
  while not fixed:
    if lst.index(lastused) == s.index(lastused): fixed = True
    else:
      ind = lst.index(lastused)
      lst[lst.index(lastused)],lst[s.index(lastused)] = lst[s.index(lastused)], lst[lst.index(lastused)]
      lastused = lst[ind]
      steps+=1
  return steps

