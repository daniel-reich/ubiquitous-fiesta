
def how_bad(n):
  x = sum(1 for x in str(bin(n)) if x == '1')
  l = []
  if x % 2 == 0:
    l.append("Evil")
  else:
    l.append("Odious")
  if all(x % n != 0 for n in range(2, x)) and (x > 1):
    l.append("Pernicious")
  return l

