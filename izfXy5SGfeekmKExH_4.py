
def puzzle_pieces(a1, a2):
 return len(set([sum(i) for i in list(zip(a1,a2))]))==1 and len(a1)==len(a2)

