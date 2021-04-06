
def solve(a, b):
  
  ##############################
  # ALGEBRAIC SHUFFLING
  ##############################
  # ax+1    =   b+x
  # ax      =   b+x-1
  # ax      =   (b-1) + x
  # ax - x  =   (b-1)
  # (a-1)x  =   (b-1)
  # ...therefore
  # x = (b-1) / (a-1)
  
  Test_A = a - 1
  Test_B = b - 1
  
  if (Test_B == 0):
    return "Any number"
  elif (Test_A == 0):
    return "No solution"
  else:
    return round(Test_B / Test_A,3)

