
def license_plate(s, n):
  chars = [char for char in s.upper() if char != '-']
  m = len(chars)
  r = m%n
  
  pieces = ([chars[:r]] if r else []) + [chars[i:i+n] for i in range(r,m,n)]
  
  return '-'.join([''.join(piece) for piece in pieces])

