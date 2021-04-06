
def largest_even(r, n=-1):
  if not r: return n
  n = [n, r[0]][not r[0] & 1 and r[0] > n]
  return largest_even(r[1:], n)

