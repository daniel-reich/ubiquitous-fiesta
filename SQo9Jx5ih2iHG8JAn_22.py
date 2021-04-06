
def expanded_form(num):
  
  Blocks = []
  Remaining = num
  
  Deduction = 1
  Divisor = 10
  
  while (Remaining > 0):
    
    Total = 0
    
    while (Remaining % Divisor != 0):
      Remaining -= Deduction
      Total += Deduction
    
    if (Total != 0):
      Blocks.insert(0, str(Total))
    
    Deduction *= 10
    Divisor *= 10
    
  Link = " + "
  Answer = Link.join(Blocks)
  return Answer

