
def puzzle_pieces(a1, a2):
  if len(a1) != len(a2):
    return False
  lst = []
  for i in range(0, len(a1)): 
      x = a1[i] + a2[i]
      if x not in lst:
        lst.append(x)
  return len(lst) == 1

