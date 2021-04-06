
def check_pattern(lst, pattern):
  lst = list(map(tuple, lst))
  return len(set([(a, b) for a, b in zip(lst, pattern)])) == len(set(pattern)) == len(set(lst))

