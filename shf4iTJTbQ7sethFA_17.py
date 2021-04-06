
def magic_square_game(alice, bob):
  
  Arow = int(alice[0])
  Bcol = int(bob[0])
  
  aint = eval('+'.join(list(alice[1])))
  bint = eval('+'.join(list(bob[1])))
  
  if aint % 2 == 0 or bint % 2 != 0:
    return False
  else:
    aimp = alice[1][Bcol - 1]
    bimp = bob[1][Arow - 1]
    
    return aimp == bimp

