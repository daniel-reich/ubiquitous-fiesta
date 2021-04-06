
def count_boomerangs(lst):
  count = 0
  for a, b, c in zip(lst, lst[1:], lst[2:]):
    if a == c and a != b:
      count += 1
  return count

