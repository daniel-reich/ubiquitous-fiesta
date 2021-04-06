
def find_a_seat(n, r):
  for i, x in enumerate(r):
    if x <= n//len(r)//2: return i
  return -1

