
def is_undulating(n):
  n = str(n)
  return len(n) >= 3 and len(set(n)) == 2 and (n[0]*2) not in n and (n[1]*2) not in n

