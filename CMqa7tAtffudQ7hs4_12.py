
def sorting_steps(lst, start=0, end=None):
  if end is None: 
    end = len(lst)
    lst =lst[:]
  if end - start < 2: return []
  swaps = []
  pivot = lst[start]
  pIdx = start
  for i in range(start + 1, end):
    if lst[i] < pivot:
      # swap i, pIdx
      swaps.append( (i, pIdx) )
      lst[i], lst[pIdx] = lst[pIdx], lst[i]
      # swap swap i, pIdx + 1
      swaps.append((i, pIdx + 1))
      lst[i], lst[pIdx + 1] = lst[pIdx + 1], lst[i]
      pIdx += 1
  return swaps + sorting_steps(lst, start, pIdx) + sorting_steps(lst, pIdx + 1, end)

