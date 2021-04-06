
def is_undulating(n):
  s,l=str(n),len(str(n))
  return n>100 and s==(s[:2]*l)[:l]

