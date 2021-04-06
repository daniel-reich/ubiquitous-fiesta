
def dice_score(lst):
  a = (lst.count(1) == 3) * 1000
  b = (lst.count(6) == 3) * 600
  c = (lst.count(5) == 3) * 500
  d = (lst.count(4) == 3) * 400
  e = (lst.count(3) == 3) * 300
  f = (lst.count(2) == 3) * 200
  g = (0 < lst.count(1) < 3) * 100
  h = (0 < lst.count(5) < 3) * 50
  return a + b + c + d + e + f + g + h

