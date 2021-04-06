
def is_ladder_safe(ldr):
  if len(ldr[0]) < 5:
    return False
​
  width = len(ldr[0])
  if (all(x == "#" * width or x == "#" + " " * (width - 2) + "#" for x in ldr) and
    "#" + " " * (width - 2) + "#" in ldr and
    "#" * width in ldr):
    
    height = len(ldr)
    rungs = [i for i in range(height) if ldr[i] == "#" * width]
    gap = rungs[1] - rungs[0] - 1
​
    if gap > 2 or any(rungs[i+1] - rungs[i] != rungs[1] - rungs[0] for i in range(len(rungs)-1)):
      return False
    else:
      return True
  
  return False

