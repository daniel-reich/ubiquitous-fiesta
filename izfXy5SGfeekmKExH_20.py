
def puzzle_pieces(a1, a2):
  x=[a1[i]+a2[i] for i in range(min(len(a1),len(a2)))]
  return all([x[i]==x[i-1] for i in range(1,min(len(a1),len(a2)))]) and len(a1)==len(a2)

