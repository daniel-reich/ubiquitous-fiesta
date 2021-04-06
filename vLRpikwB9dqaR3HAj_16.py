
def is_ord_sub(smlst, biglst):
  
  Sublist = []
  
  BC = 0
  BL = len(biglst)
  
  SC = 0
  SL = len(smlst)
  
  while (SC < SL) and (BC < BL):
    
    Wanted = smlst[SC]
    Checking = biglst[BC]
    
    if (Wanted == Checking):
      Sublist.append(Wanted)
      SC += 1
      BC += 1
    else:
      BC += 1
  
  Test_1A = len(smlst)
  Test_1B = len(Sublist)
  
  if (Test_1A == Test_1B):
    return True
  else:
    return False

