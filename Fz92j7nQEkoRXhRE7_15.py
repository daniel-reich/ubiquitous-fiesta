
def jumping_frog(n, stones):
  return jump(n, stones, pos=0, jumps=1) or 'no chance :-('
  
def jump(n, lst, pos, jumps):
  if pos >= n: 
    return jumps
  if pos < 0 or not lst[pos] or jumps == 20: 
    return False
    
  back = jump(n, lst, pos-lst[pos], jumps+1)
  forw = jump(n, lst, pos+lst[pos], jumps+1)
  
  return min((i for i in (back, forw) if i), default=False)

