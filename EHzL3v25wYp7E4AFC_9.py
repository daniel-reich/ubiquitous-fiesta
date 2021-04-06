
def can_build(s1, s2):
  
  Selection = s1
  Needed = s2
  
  S_Blocks = list(Selection)
  N_Blocks = list(Needed)
  
  Passage = ""
  
  NC = 0
  NL = len(N_Blocks)
  
  while (NC < NL):
    
    Wanted = str(N_Blocks[NC])
        
    Cursor = 0
    Span = len(S_Blocks)
      
    while (Cursor < Span):
        
      Item = str(S_Blocks[Cursor])
        
      if (Item == Wanted):
        Passage = Passage + str(Item)
        S_Blocks[Cursor] = "999"
        Cursor += Span
      else:
        Cursor += 1
        
    while ("999" in S_Blocks):
      S_Blocks.remove("999")
  
    NC += 1
  
  if (Passage == Needed):
    return True
  else:
    return False

