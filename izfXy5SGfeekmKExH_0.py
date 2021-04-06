
def puzzle_pieces(a1, a2):
  return len(a1)==len(a2) and len(set(a1[i]+a2[i] for i in range(len(a1))))==1

