
def puzzle_pieces(a1, a2):
  if len(a1)!=len(a2):
    return False
  else:
    for i in range(len(a1)):
      a1[i] += a2[i]
    return True if len(set(a1))==1 else False

