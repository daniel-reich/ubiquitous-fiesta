
def is_super_d(n):
  
  Tester = 2
  
  while (Tester <= 9):
    
    Super_D = Tester * (n ** Tester)
    
    Sample = str(Super_D)
    Excerpt = str(Tester) * Tester
    
    if (Excerpt in Sample):
      return "Super-" + str(Tester) + " Number"
    else:
      Tester += 1
  
  return "Normal Number"

