
def min_swaps(s1, s2):
  count = 0
  for l1,l2 in zip(s1,s2):
    if l1 != l2: count += 1
  return count//2

