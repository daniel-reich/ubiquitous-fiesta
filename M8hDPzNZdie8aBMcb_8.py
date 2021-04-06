
def count_substring(txt):
  a_idx = [idx for idx, char in enumerate(txt) if char=='A']
  x_idx = [idx for idx, char in enumerate(txt) if char=='X']
  return sum([1 for a in a_idx for x in x_idx if a<x])

