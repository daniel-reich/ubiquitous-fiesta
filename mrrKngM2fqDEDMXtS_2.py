
def can_patch(bridge, planks):
  gaps = [i for i in ''.join(map(str, bridge)).split('1') if len(i) != 0]
  
  for gap in gaps:
    gap_filled = False
    
    if len(gap) == 1:
        gap_filled = True
        
    else:
      for plank in sorted(planks):
        if len(gap) - plank < 2:
          planks.remove(plank)
          gap_filled = True
          break
      
    if not gap_filled:
      return False
    
  return True

