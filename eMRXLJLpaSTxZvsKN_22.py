
def is_ladder_safe(ldr):
  w = len(ldr[0])
  lev_ok = all(lev in ["#"*w,"#"+" "*(w-2)+"#"] for lev in ldr)
  rungs = [i for i in range(len(ldr)) if ldr[i] == "#"*w]
  spaced_ok = rungs in [[i for i in range(1,len(ldr)-1)],[i for i in range(1,len(ldr)-1,3)]]
  return w>4 and lev_ok and spaced_ok

