
def bishop(start, end, n):
  pos = lambda p: (ord(p[0]) - ord('a'), int(p[1]) - 1)
  r1, c1 = pos(start)
  r2, c2 = pos(end)
  if (r1 + c1) % 2 != (r2 + c2) % 2:
    return False
  elif n == 0:
    return start == end
  elif n == 1:
    return abs(r1 - r2) == abs(c1 - c2)
  else:
    return True

