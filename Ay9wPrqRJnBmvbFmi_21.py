
def halve_count(a, b, cnt=0):
  if a/2 <= b: return cnt
  return halve_count(a/2, b, cnt+1)

