
def can_capture(queens):
  a1, a2 = queens[0]
  b1, b2 = queens[1]
  c = abs(ord(a1) - ord(b1)) == abs(int(a2) - int(b2))
  return c or any(x in queens[1] for x in queens[0])

