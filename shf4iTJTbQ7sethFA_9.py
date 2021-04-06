
def magic_square_game(alice, bob):
  mem=[ [9,9,9],  [9,9,9],  [9,9,9] ]
  mem[alice[0]-1]=[int(i) for i in alice[1]]
  for i in range(3):
    if mem[i][bob[0]-1]!=int(bob[1][i]) and mem[i][bob[0]-1]!=9:
      return False
  return True

