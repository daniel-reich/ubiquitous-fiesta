
def puzzle_pieces(a1, a2):
  return len(set([x+y for x,y in zip(a1,a2) ]))==1 and len(a1)==len(a2)

