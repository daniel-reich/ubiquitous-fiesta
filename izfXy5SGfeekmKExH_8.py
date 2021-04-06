
def puzzle_pieces(a1, a2):
  return False if len(a1)!=len(a2) else all(a1[i]+a2[i]==a1[i+1]+a2[i+1] for i in range(len(a1)-1))

