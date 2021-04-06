
def bishop(start, end, n):
  BorW = lambda pos: (ord(pos[0]) + ord(pos[1])) % 2
  
  if n == 0: return start == end
  if BorW(start) != BorW(end): return False
  xofs = abs(ord(start[0]) - ord(end[0]))
  yofs = abs(ord(start[1]) - ord(end[1]))
  return (1 if xofs == yofs else 2) <= n

